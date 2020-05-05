<script>
    import { nameFacet, typeFacet, mapGlobal, renderedKeysGlobal } from './store';

    export let request;
    let checkedFacets = {
        'names': [],
        'types': []
    };

    let respondedItems = {};

    const updateDrawItems = () => {

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
                    items.forEach(item => {
                        let objItem;
                        eval('objItem='+item[0]);
                        let keys = Object.keys(objItem);

                        keys.forEach(key => {
                            respondedItems[key] = objItem[key];
                        });
                    })
                })
                .then(_ => {
                    drawPoly();
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
        updateDrawItems();
    });
    typeFacet.subscribe(newValue => {
        combineFacets(newValue, 'types');
        updateDrawItems();
    });

    const getRandomColor = () => {
        const h = Math.random() * (360);
        const s = Math.random() * (101 - 80) + 80;
        const l = 50;

        return `hsl(${h}, ${s}%, ${l}%)`
    };

    const getBounds = function (poly) {
        let lat_arr = [];
        for (let ii = 0; ii < poly.length; ii++) {
            lat_arr.push(poly[ii].lat);
        }

        let lon_arr = [];
        for (let ii = 0; ii < poly.length; ii++) {
            lon_arr.push(poly[ii].lng);
        }

        let zoom = new google.maps.LatLngBounds(
            new google.maps.LatLng(Math.max(...lat_arr), Math.min(...lon_arr)),
            new google.maps.LatLng(Math.min(...lat_arr), Math.max(...lon_arr))
        );

        return (zoom);
    };

    const drawPoly = () => {
        const keys = Object.keys(respondedItems);
        const renderedKeys = Object.keys($renderedKeysGlobal)

        console.log('rendered', renderedKeys, 'keys', keys)

        const notRenderedKeys = keys.filter(e => !renderedKeys.includes(e))
        console.log('not render', notRenderedKeys)

        notRenderedKeys.forEach(key => {
            let polygons = respondedItems[key]['poly'];
            let centroid = respondedItems[key]['centroid'];

            const color = getRandomColor();
            console.log(color)
            const zoom = getBounds(polygons[0]);

            polygons.forEach(poly => {
                let mapPoly = new google.maps.Polygon({
                    paths: poly,
                    strokeColor: color,
                    strokeOpacity: 0.8,
                    strokeWeight: 1,
                    fillColor:  color,
                    fillOpacity: 0.2,
                    zIndex: renderedKeys.length
                });
                mapPoly.setMap($mapGlobal);
                $mapGlobal.fitBounds(zoom);
                $mapGlobal.setCenter({lat: centroid.lat, lng: centroid.lng});
                let polyObject = {};
                polyObject[key] = mapPoly;
                renderedKeysGlobal.addKey(polyObject)
            })
        });



        const extraKeys = renderedKeys.filter(e => !keys.includes(e))
        extraKeys.forEach(key => {
            $renderedKeysGlobal[key].setMap(null);
            renderedKeysGlobal.deleteKey(key);

        });

    }
</script>