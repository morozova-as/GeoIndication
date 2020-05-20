<script>
    import {
        nameFacet,
        typeFacet,
        mapGlobal,
        renderedKeysGlobal,
        globalAction,
        alertState,
        isInitState,
        stateInfoPanel,
        loadingState
    } from './store';
    import {getBounds} from '../utils'


    export let request;

    let checkedFacets = {
        'names': $nameFacet,
        'types': $typeFacet
    };

    let respondedItems = {};
    let numberItems = 0;
    let changedFacet = '';

    const fixJSONObject = (str) => {
        let temp = str;
        temp = temp.replace(/'/g, '')
        temp = temp.replace(/"/g, '')
        temp = temp.replace(/lat/g, '"lat"');
        temp = temp.replace(/lng/g, '"lng"');
        temp = temp.replace(/label/g, '"label"');
        temp = temp.replace(/poly/g, '"poly"');
        temp = temp.replace(/, centroid/g, '", "centroid"');
        return temp.replace(/(\d+): {"label": /g, '"$1": {"label": "');
    }

    export const updateDrawItems = () => {
        loadingState.set(true)

        const fetchPromise = fetch(request, {
            method: 'POST',
            body: JSON.stringify(checkedFacets)
        });

        respondedItems = {}

        fetchPromise
                .then(response => response.json())
                .then(items => {
                    if (!items)
                        return;

                    numberItems = 0;
                    items.forEach(item => {
                        let polyRespond;
                        // respond = JSON.parse(fixJSONObject(item[0]))
                        eval('polyRespond=' + item[0]);

                        const numRespond = item[1];

                        let keys = Object.keys(polyRespond);

                        respondedItems[numRespond] = {};

                        keys.forEach(key => {
                            respondedItems[numRespond][key] = {
                                'num': numberItems,
                                'info': polyRespond[key]
                            };
                        });
                        numberItems += 1;
                    })
                })
                .then(_ => {
                    loadingState.set(false)
                    drawPoly();
                    globalAction.set(0)
                })
                .catch(e => {
                    console.warn(e);
                })

    }

    const combineFacets = (value, key) => {
        checkedFacets[key] = value;
    };


    nameFacet.subscribe(newValue => {
        combineFacets(newValue, 'names');
        changedFacet = 'name';
        if ($globalAction)
            updateDrawItems();
    });
    typeFacet.subscribe(newValue => {
        combineFacets(newValue, 'types');
        changedFacet = 'type';
        if ($globalAction)
            updateDrawItems();
    });

    const getRandomColor = (n) => {
        const getColor = () => {
            const h = Math.random() * (360);
            const s = Math.random() * (101 - 80) + 80;
            const l = 50;
            return `hsl(${h}, ${s}%, ${l}%)`
        }

        let colorsArray = [];

        for (let i = 0; i < n; i++)
            colorsArray.push(getColor());

        return colorsArray
    };


    const handleClick = (key) => {
        if (!$stateInfoPanel) {
            stateInfoPanel.set(true);

            document.body.addEventListener('panel-opened', () => {
                document.body.dispatchEvent(new CustomEvent('click-polygon', {detail: key}))
            }, {once: true, passive: true})
        } else {
            document.body.dispatchEvent(new CustomEvent('click-polygon', {detail: key}))
        }

    }

    const drawPoly = () => {
        const keys = Object.keys(respondedItems);
        const renderedKeys = Object.keys($renderedKeysGlobal)

        const notRenderedKeys = keys.filter(e => !renderedKeys.includes(e))

        const colors = getRandomColor(numberItems);

        let allPolys = []
        notRenderedKeys.forEach(key => {
            const idNotRendered = Object.keys(respondedItems[key]);

            if (idNotRendered.length === 0) {
                renderedKeysGlobal.addEmptyData(key)
                if (notRenderedKeys.length === 1 && !$isInitState)
                    alertState.set(true)
            }

            idNotRendered.forEach(idToRender => {
                let polygons = respondedItems[key][idToRender]['info']['poly'];
                let centroid = respondedItems[key][idToRender]['info']['centroid'];

                let centroids = [];
                let mapPolys = [];
                polygons.forEach(poly => {
                    let mapPoly = new google.maps.Polygon({
                        paths: poly,
                        strokeColor: colors[respondedItems[key][idToRender]['num']],
                        strokeOpacity: 0.8,
                        strokeWeight: 1,
                        fillColor: colors[respondedItems[key][idToRender]['num']],
                        fillOpacity: 0.2,
                        zIndex: renderedKeys.length,
                        map: $mapGlobal
                    });

                    $mapGlobal.setCenter({lat: centroid.lat, lng: centroid.lng - 0.05});

                    mapPolys.push(mapPoly);
                    allPolys.push(mapPoly)
                    centroids.push({lat: centroid.lat, lng: centroid.lng - 0.05})
                })

                mapPolys.forEach(poly => {
                    google.maps.event.addListener(poly, 'click', e => {
                        handleClick(key);
                    });
                })

                renderedKeysGlobal.addPoly(key, idToRender, mapPolys)
                renderedKeysGlobal.addCentroid(key, centroids)
            })
        });

        if (allPolys.length !== 0)
            $mapGlobal.fitBounds(getBounds(allPolys));


        const extraKeys = renderedKeys.filter(e => !keys.includes(e))

        extraKeys.forEach(key => {
            if (Object.keys($renderedKeysGlobal[key]).length !== 0) {
                const objToDel = $renderedKeysGlobal[key]['poly'];
                const idToDel = Object.keys(objToDel);
                idToDel.forEach(id => {
                    objToDel[id].forEach(e => e.setMap(null))
                });
            }
        });

        renderedKeysGlobal.deleteKeys(extraKeys);
    }


</script>