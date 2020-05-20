<script>

    import {renderedKeysGlobal, mapGlobal, alertState, loadingState, imageGlobal} from './store'
    import {getBounds} from '../utils'
    import {onDestroy, onMount} from 'svelte';

    export let key;
    export let manufacturers;
    let nameManufacturer;
    let status;
    let description;
    let href;
    let hoverFlag = false

    let component;
    // import placeholder from "../placeholder.jpg"


    export let state = true;
    let imgUrl = "./images/placeholder.jpg";


    const { protocol, hostname } = window.location;
    const baseURL = `${protocol}//${hostname}:8000/`;

    const fetchPromise = fetch(`${baseURL}get_image_for_product/`, {
        method: 'POST',
        body: JSON.stringify(key)
    });


    fetchPromise
            .then(response => response.blob())
            .then(response => {
                imgUrl = URL.createObjectURL(response)
            })
            .catch(e => console.warn(e))

    const handleClick = (e) => {
        let keyClick = e.detail;
        if (key !== keyClick)
            return;

        if (state)
            state = false;

        component.scrollIntoView({block: "start", behavior: "smooth"})
    }


    const toggleInfo = () => {
        state = !state;
    }

    const showOnMap = () => {
        let currObj = $renderedKeysGlobal[key];
        if (Object.keys(currObj).length === 0) {
            alertState.set(true)
        } else {

            let allPolys = []
            let polysClick = Object.keys(currObj['poly'])
            let flag = 1;

            polysClick.forEach(key => {
                currObj['poly'][key].forEach(poly => {
                    allPolys.push(poly)
                })
            })

            if (polysClick.length !== 0) {
                $mapGlobal.fitBounds(getBounds(allPolys));
                $mapGlobal.setCenter(getBounds(allPolys).getCenter())

                allPolys.forEach(poly => {
                    poly.setOptions({'fillOpacity': 0.5});
                })
                setTimeout(() => {
                    allPolys.forEach(poly => {
                        poly.setOptions({'fillOpacity': 0.2});
                    })
                }, 1000)
            }
        }
    }

    onMount(() => {
        document.body.addEventListener('click-polygon', handleClick)
    })

    onDestroy(() => {
        document.body.removeEventListener('click-polygon', handleClick)
    })

    const onImageEnter = () => {
        hoverFlag = true
        setTimeout(() => {
            if (hoverFlag)
                imageGlobal.set(imgUrl)
        }, 500)

    }

    const onImageLeave = () => {
        hoverFlag = false
        imageGlobal.set('')
    }

</script>


<style>

    .info-item {
        /*width: 100%;*/
        /*overflow: hidden;*/

        /*width: 300px;*/
        /*margin-right: 10px;*/
        padding-top: 10px;
        background: #ffffff;
        border-radius: 4px;

        box-shadow: 0 8px 6px -6px rgba(0, 0, 0, 0.12);
        transition: all 0.3s cubic-bezier(.25, .8, .25, 1);
    }

    .info-item:hover {
        box-shadow: 0 10px 6px -6px rgba(0, 0, 0, 0.12);
    }

    .item-name {
        align-self: center;
        text-align: left;

        font-weight: 600;
        font-size: 14px;
        line-height: 20px;
    }

    .item-head {
        display: grid;
        grid-template-columns: auto 20px;
        grid-column-gap: 20px;

        padding: 0 10px 10px;
    }

    .item-img-container {
        height: 50px;
        width: 50px;
        padding-right: 15px;
    }

    .item-img {
        /*height: 50px;*/

        /*width: 50px;*/
        height: 100%;
        width: 100%;
        min-width: 50px;
        object-fit: contain;
    }

    .click-button {
        background: transparent;
        border: none;
        padding: 0;
        margin: 0;
        cursor: pointer;

        position: relative;

        display: flex;
    }

    .click-button:not(:disabled):active {
        background: initial;
    }


    .toggle-button {
        background: transparent;
        border: none;
        padding: 0;
        margin: 0;
        cursor: pointer;
        width: 20px;
        height: 20px;
    }

    .toggle-button-reverse {
        transform: rotate(180deg);
    }

    .toggle-button:not(:disabled):active {
        background: initial;
        transform: scale(0.9);
    }

    .toggle-button-icon {
        height: 100%;
        width: 100%;
        transform: rotate(-90deg);
    }

    .status {
        height: 20px;
        width: 20px;
        border-radius: 50%;
        display: inline-block;
        position: relative;
    }

    .status__red {
        background-color: #da4f4f;
    }

    .status__green {
        background-color: #6daf7b;
    }

    .status__black {
        background-color: #585858;
    }

    .status__blue {
        background-color: #d3ebff;
    }

    .manufacturer {
        padding: 20px 10px;
        background: #dadada26;
    }

    .manufacturer-info {
        display: grid;
        grid-column-gap: 10px;
        grid-template-columns: 20px auto;
    }


    .description {
        margin-top: 15px;
        color: #525252;
        font-size: 14px;
        line-height: 18px;
        font-weight: 300;
    }

    .address {
        color: #3c3c3c;
        font-weight: 600;

        font-size: 14px;
        line-height: 18px;
    }

    .click-link {
        display: inline-flex;
        position: relative;

        height: 15px;
        margin-left: 7px;
        vertical-align: middle;
    }

    .click-icon {
        display: inline;

        height: 100%;
    }

    .tooltip {
        visibility: hidden;
        position: absolute;
        width: 150px;
        background-color: #555;
        color: #fff;
        text-align: center;
        padding: 5px 0;
        font-weight: 300;
        border-radius: 6px;
        z-index: 1;
        opacity: 0;
        transition: opacity 0.3s;
        top: calc(100% + 7px);
        margin-left: -60px;
    }

    .tooltip__click {
        left: 15px;
        width: 130px;
    }

    .tooltip__show {
        left: calc(50% - 35px);
    }

    .tooltip__status {
        left: 0;
        margin-left: 0;
    }

    .tooltip::after {
        content: "";
        position: absolute;
        bottom: 100%;
        left: 50%;
        margin-left: -5px;
        border-width: 5px;
        border-style: solid;
        border-color: transparent transparent #555 transparent
    }

    .tooltip__status::after {
        left: 7%;
    }

    .tooltip__click::after {
        left: 40%;
    }

    .click-link:hover .tooltip__click, .item-name:hover + .tooltip__show, .status:hover .tooltip__status {
        visibility: visible;
        opacity: 1;
    }

    .info-item:last-child {
        margin-bottom: 50px;
    }

    .geo-text {
        padding: 10px;
        font-size: 12px;
        font-weight: 300;
        display: grid;
        grid-template-columns: 20px auto;
        grid-column-gap: 10px;
    }

    .description-text {
        padding: 10px;
        font-size: 14px;
        font-weight: 300;
    }

    .geo-icon {
        width: 20px;
        height: 20px;
    }


</style>


{#if manufacturers}
    <div class="info-item" bind:this={component}>


        <div class="item-head">
            <button class="click-button"
                    on:click={showOnMap}
            >
                <div class="item-img-container" on:mouseenter={onImageEnter} on:mouseleave={onImageLeave}>
                    <img class="item-img" src={imgUrl} alt="image of product" aria-hidden/>
                </div>


                <span class="item-name">
                    {manufacturers[0].name}
                </span>

                <span class="tooltip tooltip__show">Посмотреть на карте</span>
            </button>

            <!--            {#if manufacturers[0].manufacturer}-->
            <button class="toggle-button" class:toggle-button-reverse={!state} on:click={toggleInfo}>
                <svg fill="#333" class="toggle-button-icon" viewBox="0 0 10 16" xmlns="http://www.w3.org/2000/svg">
                    <path d="M0 8l8-8 1.5 1.5L3 8l6.5 6.5L8 16 0 8z"></path>
                </svg>
            </button>
            <!--            {/if}-->
        </div>

        {#if !state}


            <div class="description-text">
                {manufacturers[0].main_description}
                <a class="click-link" target='_blank' href={manufacturers[0].main_href}>
                    <svg fill="#333" class="click-icon" xmlns="http://www.w3.org/2000/svg"
                         viewBox="0 0 511.63 511.63">
                        <defs/>
                        <path d="M392.86 292.35h-18.28c-2.67 0-4.86.86-6.56 2.58a8.86 8.86 0 00-2.57 6.56v91.36c0 12.56-4.47 23.32-13.42 32.26-8.94 8.95-19.7 13.42-32.26 13.42H82.22c-12.56 0-23.31-4.47-32.26-13.42-8.95-8.94-13.42-19.7-13.42-32.26V155.31c0-12.56 4.47-23.31 13.42-32.26s19.7-13.42 32.26-13.42h201a8.9 8.9 0 006.57-2.57 8.9 8.9 0 002.56-6.56V82.22c0-2.66-.85-4.85-2.56-6.56a8.89 8.89 0 00-6.57-2.57h-201c-22.64 0-42.01 8.04-58.1 24.13C8.04 113.3 0 132.66 0 155.31v237.53c0 22.65 8.04 42.02 24.12 58.1 16.09 16.08 35.46 24.13 58.1 24.13h237.55c22.65 0 42.02-8.05 58.1-24.13S402 415.5 402 392.85V301.5c0-2.67-.86-4.86-2.58-6.57a8.88 8.88 0 00-6.56-2.58z"/>
                        <path d="M506.2 41.97a17.57 17.57 0 00-12.85-5.42H347.17c-4.95 0-9.23 1.8-12.85 5.42-3.61 3.62-5.42 7.9-5.42 12.85s1.8 9.23 5.42 12.85l50.25 50.25-186.15 186.15a9.02 9.02 0 00-2.85 6.56c0 2.48.95 4.67 2.85 6.57l32.55 32.55c1.9 1.9 4.1 2.85 6.57 2.85s4.66-.95 6.57-2.86L430.25 163.6l50.26 50.25c3.6 3.61 7.9 5.42 12.84 5.42s9.23-1.8 12.85-5.43a17.55 17.55 0 005.43-12.84V54.82c0-4.95-1.82-9.23-5.43-12.85z"/>
                    </svg>

                    <div class="tooltip tooltip__click">Посмотреть свидетельство</div>
                </a>
            </div>

            <div class="geo-text">
                <svg fill="#333" class="geo-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                    <defs/>
                    <g fill="#231F20">
                        <path d="M313.9 376.7c41.3-68.5 93.5-164.8 93.5-214.3C407.4 78.9 339.5 11 256 11S104.6 78.9 104.6 162.4c0 49.5 52.2 145.8 93.5 214.3-49 3.7-160.5 17-160.5 61.1 0 43.4 113.2 63.2 218.5 63.2 105.2 0 218.5-19.8 218.5-63.2-.1-44.1-111.7-57.4-160.7-61.1zM125.5 162.4c0-72 58.6-130.6 130.5-130.6 72 0 130.6 58.6 130.6 130.6 0 62.9-100.2 220.7-130.6 267.1-30.4-46.4-130.5-204.2-130.5-267.1zM256 480.1c-127.9 0-197.6-28-197.6-42.4 0-11.1 46-35 152-41.1 19.9 32.1 35 54.8 37 57.5 2.7 3.6 10.6 7.9 17.3 0 2.1-2.5 17.1-25.4 37-57.5 106 6.1 152 29.9 152 41.1-.1 14.5-69.8 42.4-197.7 42.4z"/>
                        <path d="M321.9 162.4A65.9 65.9 0 00256 96.5a65.9 65.9 0 00-65.9 65.9 65.9 65.9 0 0065.9 65.9 65.9 65.9 0 0065.9-65.9zm-111 0a45.11 45.11 0 0190.2 0 45.11 45.11 0 01-90.2 0z"/>
                    </g>
                </svg>
                {manufacturers[0].main_geo_text}
            </div>

            {#each manufacturers as item, num }

                {#if item.manufacturer}

                    <div class="manufacturer">


                        <div class="manufacturer-info">

                            <div class="status" class:status__red={item.status === 'Срок действия истек'}
                                 class:status__green={item.status === 'Действует'}
                                 class:status__black={item.status === 'Прекратил действие'}
                                 class:status__blue={item.status === 'Нет данных'}>

                                <div class="tooltip tooltip__status">
                                    {item.status}
                                </div>
                            </div>

                            <div class="address">
                                {item.manufacturer}
                                <a class="click-link" target='_blank' href={item.href}>
                                    <svg fill="#333" class="click-icon" xmlns="http://www.w3.org/2000/svg"
                                         viewBox="0 0 511.63 511.63">
                                        <defs/>
                                        <path d="M392.86 292.35h-18.28c-2.67 0-4.86.86-6.56 2.58a8.86 8.86 0 00-2.57 6.56v91.36c0 12.56-4.47 23.32-13.42 32.26-8.94 8.95-19.7 13.42-32.26 13.42H82.22c-12.56 0-23.31-4.47-32.26-13.42-8.95-8.94-13.42-19.7-13.42-32.26V155.31c0-12.56 4.47-23.31 13.42-32.26s19.7-13.42 32.26-13.42h201a8.9 8.9 0 006.57-2.57 8.9 8.9 0 002.56-6.56V82.22c0-2.66-.85-4.85-2.56-6.56a8.89 8.89 0 00-6.57-2.57h-201c-22.64 0-42.01 8.04-58.1 24.13C8.04 113.3 0 132.66 0 155.31v237.53c0 22.65 8.04 42.02 24.12 58.1 16.09 16.08 35.46 24.13 58.1 24.13h237.55c22.65 0 42.02-8.05 58.1-24.13S402 415.5 402 392.85V301.5c0-2.67-.86-4.86-2.58-6.57a8.88 8.88 0 00-6.56-2.58z"/>
                                        <path d="M506.2 41.97a17.57 17.57 0 00-12.85-5.42H347.17c-4.95 0-9.23 1.8-12.85 5.42-3.61 3.62-5.42 7.9-5.42 12.85s1.8 9.23 5.42 12.85l50.25 50.25-186.15 186.15a9.02 9.02 0 00-2.85 6.56c0 2.48.95 4.67 2.85 6.57l32.55 32.55c1.9 1.9 4.1 2.85 6.57 2.85s4.66-.95 6.57-2.86L430.25 163.6l50.26 50.25c3.6 3.61 7.9 5.42 12.84 5.42s9.23-1.8 12.85-5.43a17.55 17.55 0 005.43-12.84V54.82c0-4.95-1.82-9.23-5.43-12.85z"/>
                                    </svg>

                                    <div class="tooltip tooltip__click">Посмотреть свидетельство</div>
                                </a>


                            </div>


                        </div>

                        <div class="description">
                            {item.description}
                        </div>


                    </div>

                {/if}

            {/each}

        {/if}


    </div>
{/if}