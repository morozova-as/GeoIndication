<script>
    import {mapGlobal, nameFacet, renderedKeysGlobal, loadingState, globalAction} from './store'

    export let state = false;
    export let requestUrl;
    let mapListener = null

    const handleClick = (mapsMouseEvent) => {
        const latLng = mapsMouseEvent.latLng;

        loadingState.set(true)

        const fetchPromise = fetch(requestUrl, {
            method: "POST",
            body: JSON.stringify({lat: latLng.lat(), lng: latLng.lng()})
        });

        fetchPromise
                .then(response => response.json())
                .then(response => {
                    globalAction.set(1)
                    nameFacet.addData(response)
                    state = false;
                    loadingState.set(false)
                    togglePolygon(true);
                    mapListener.remove();
                })
    }

    const togglePolygon = (state) => {
        const renderedKeys = Object.keys($renderedKeysGlobal);
        if (renderedKeys.length !== 0) {
            renderedKeys.forEach(key => {
                if (Object.keys($renderedKeysGlobal[key]).length > 0) {
                    const objToHide = $renderedKeysGlobal[key]['poly'];

                    const idToHide = Object.keys(objToHide);
                    idToHide.forEach(id => {
                        objToHide[id].forEach(e => e.setVisible(state))
                    });
                }
            })
        }
    }

    const toggleFinder = () => {
        state = !state;

        if (state) {
            togglePolygon(false);
            mapListener = $mapGlobal.addListener('click', handleClick, {once: true});
        } else {
            if (mapListener)
                mapListener.remove();

            togglePolygon(true);

        }

    }
</script>

<style>
    .finder-button {
        position: fixed;
        top: 130px;
        right: 6px;
        width: 50px;
        height: 50px;
    }

    .finder-button .button {
        padding: 10px 10px 5px;
        background: #fff;
        border-radius: 4px;
        box-shadow: 0 8px 20px rgba(68, 75, 91, 0.2);
    }

    .finder-button .button:hover {
        background: #f3f3f3;
    }

    .finder-button-active .button {
        background: #98c1a1 !important;
    }

    .finder-button .button:not(:disabled):active {
        background: #fff;
        transform: scale(0.95);
    }

    .button {
        background: transparent;
        border: none;
        padding: 0;
        margin: 0;
        cursor: pointer;
    }

    .button-icon {
        height: 100%;
        width: 100%;
    }

    .tooltip {
        visibility: hidden;
        position: absolute;
        width: 350px;
        background-color: #555;
        color: #fff;
        text-align: center;
        font-weight: 300;
        border-radius: 6px;
        z-index: 1;
        opacity: 0;
        transition: opacity 0.3s;
        top: calc(100% + 7px);
        margin-left: -60px;
        padding: 10px;
    }

    .tooltip::after {
        content: "";
        position: absolute;
        bottom: 100%;
        left: 93%;
        margin-left: -5px;
        border-width: 5px;
        border-style: solid;
        border-color: transparent transparent #555 transparent
    }

    .tooltip__finder {
        right: 0;
    }

    .button:hover + .tooltip__finder {
        visibility: visible;
        opacity: 1;
    }
</style>


<div class="finder-button" class:finder-button-active={state}>
    <button class="button" on:click={toggleFinder}>

        <svg  fill="#333" class="button-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 490 490">
            <defs/>
            <path d="M245 490c135.31 0 245-109.69 245-245S380.31 0 245 0 0 109.69 0 245s109.69 245 245 245zm46.06-118.29c-43.5-60.11-66.8-110.7-66.8-129.7 0-44.63 24.36-70.23 66.85-70.23 42.49 0 66.86 25.6 66.86 70.23 0 21.74-27.51 74.58-66.9 129.7zM276.67 142.1c-45.17 5.3-75.48 35.74-81.74 81.74l-32 32-66.5-66.5L254.87 30.89a212.94 212.94 0 01101.8 31.2l-80 80zM245 459.37c-66.2 0-125.48-30.17-164.83-77.48l117.2-117.2c15.44 53.96 74.2 132.41 81.82 142.36l11.92 15.75 12-15.75a868.97 868.97 0 0045-66.1l51.9 51.9c-39.07 40.94-94.09 66.52-155.01 66.52zM459.38 245c0 46.25-14.77 89.08-39.77 124.14l-55.7-55.7c13.92-26.04 24.68-52.34 24.68-71.43 0-51.45-27.04-87.5-70.76-97.78l64.06-64.06c47.31 39.35 77.49 98.63 77.49 164.83zM208.69 33.76L74.77 167.7l-20.45-20.46c30.3-58.84 87-101.92 154.37-113.47zM41.5 177.72l99.77 99.77-79.18 79.18A213.05 213.05 0 0130.62 245c0-23.5 3.86-46.1 10.88-67.28z"/>
            <circle cx="288.8" cy="241.94" r="31.57"/>
        </svg>
    </button>

    <div class="tooltip tooltip__finder">Нажмите, чтобы активировать режим выбора точки на карте для поиска наименований мест происхождений товаров в выбранном районе</div>
</div>