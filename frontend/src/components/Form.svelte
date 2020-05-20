<script>
    import {} from './store'
    import {fade} from 'svelte/transition';


    export let state = false;
    export let requestGeoUrl;
    let inputName = '';
    let inputDescription = '';
    let inputGeo = '';


    const handleClick = () => {
        state = !state;
    }


    const submit = (e) => {
        e.preventDefault();

        const fetchPromise = fetch(requestGeoUrl, {
            method: 'POST',
            body: JSON.stringify(inputGeo)
        });

        fetchPromise
                .then(response => response.json())
                .then(response => console.log(response))

    }

</script>

<style>
    .wrapper {
        background: #52525270;
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 3;
    }


    .form-button {
        position: fixed;
        top: 10px;
        right: 70px;
    }

    .form-button .button {
        padding: 10px 10px;
        background: #fff;
        border-radius: 4px;
        box-shadow: 0 8px 20px rgba(68, 75, 91, 0.2);
    }

    .form-button .button:hover {
        background: #f3f3f3;
    }

    .form-button .button:not(:disabled):active {
        background: #f3f3f3;
        transform: scale(0.95);
    }

    .button {
        background: transparent;
        border: none;
        padding: 0;
        margin: 0;
        cursor: pointer;

        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
    }

    .button-icon {
        height: 30px;
        width: 30px;
        margin-right: 15px;
        margin-bottom: 5px;
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

    .form {
        width: 500px;
        padding: 50px 30px;
        position: fixed;
        max-height: calc(100vh - 200px);
        top: 100px;
        left: calc(50% - 250px);
        z-index: 2;
        background: #fff;
        border-radius: 4px;
        box-shadow: 0 8px 20px rgba(68, 75, 91, 0.2);
        box-sizing: border-box;
        overflow: scroll;
    }

    .title {
        font-size: 16px;
        line-height: 20px;
        font-weight: 600;
    }

    .close-button {
        position: absolute;
        right: 20px;
        top: 20px;
        width: 20px;
        height: 20px;
    }

    .close-button-inner {
        background: transparent;
        border: none;
        padding: 0;
        margin: 0;
        cursor: pointer;
    }

    .button-icon-close {
        height: 100%;
        width: 100%;
    }

    .close-button .close-button-inner :not(:disabled):active {
        background: transparent;
        transform: scale(0.95);
    }

    .clear-button {
        position: absolute;
        top: 0;
        right: 5px;
        width: 20px;

        padding: 0;
        background: transparent;
        outline: none;
        border: none;
        margin: 0;
        height: 20px;
        cursor: pointer;
    }

    .clear-button:active {
        background: transparent;
        transform: scale(0.95);
    }


    .clear-button-icon {
        width: 100%;
    }

    .label {
        position: relative;
        margin: 20px 0;
    }

    .label-name {
        margin-bottom: 10px;
        font-size: 14px;
        line-height: 18px;
        width: 90%;
    }

    .input {
        width: 100%;
        background: transparent;
        font-size: 16px;
        outline: none !important;
        margin: 0;
        border: 1px solid black;
        padding: 10px 10px;
        height: auto;
    }



    .input:focus {
        background: #dadada26;
    }


    .submit-button {
        background: transparent;
        cursor: pointer;
        margin: 0;
        padding: 15px;
    }

    .submit-button:hover {
        background: #dadada26;
    }


    .submit-button:active {
        outline: none;
        background: #dadada26;
        transform: scale(0.96);
    }

    .textarea{
        overflow: auto;

        resize: vertical;
        font-size: 12px;
        line-height: 20px;
    }


    .wrapper ::-webkit-scrollbar {
        width: 4px;
    }


    .wrapper ::-webkit-scrollbar-thumb {
        background-color: #a9a9a9;
        outline: 1px solid #708090;
        border-radius: 8px;
    }

</style>


<div class="form-button">
    <button class="button" on:click={handleClick}>

        <svg fill="#333" class="button-icon" xmlns="http://www.w3.org/2000/svg" viewBox="-18 -18 577.33 577">
            <defs/>
            <path d="M473.85 3.71A12.34 12.34 0 00464.99.1c-3.31.02-6.48 1.31-8.86 3.61L277.47 182.37l-.5.5-.25.25c-.24.38-.62.75-.87 1.13 0 .12-.12.12-.12.25-.25.37-.38.62-.63 1-.13.12-.13.25-.25.37-.12.37-.24.62-.37 1 0 .12-.13.12-.13.24l-31.81 95.95a12.3 12.3 0 003 12.73 12.56 12.56 0 008.85 3.61c1.35-.03 2.7-.23 4-.62l95.69-31.94c.12 0 .12 0 .24-.13.4-.1.78-.28 1.13-.5.1 0 .18-.05.25-.12.37-.25.87-.5 1.25-.75.37-.25.74-.63 1.12-.87.13-.12.25-.12.25-.25.12-.13.37-.25.5-.5L537.6 84.94a12.43 12.43 0 000-17.6zM291.7 214.31l35.3 35.31-52.9 17.6zm58.39 23.08l-46.17-46.16L465 30.16l46.16 46.16zm0 0"/>
            <path d="M444.4 233.28a12.51 12.51 0 00-12.47 12.47v233.19a37.54 37.54 0 01-37.43 37.43H62.38a37.55 37.55 0 01-37.43-37.43V146.82a37.54 37.54 0 0137.43-37.43h233.18a12.47 12.47 0 100-24.96H62.38A62.41 62.41 0 000 146.82v332.12a62.4 62.4 0 0062.38 62.38H394.5a62.4 62.4 0 0062.38-62.38V245.75a12.51 12.51 0 00-12.48-12.47zm0 0"/>
        </svg>

        Предложить новое НМПТ
    </button>

    <div class="tooltip tooltip__finder">Нажмите, чтобы заполнить форму для нового наименования места происхождения
        товара
    </div>
</div>

{#if state}
    <div class="wrapper" transition:fade="{{ duration: 300 }}">
        <form id="new-nmpt-form" class="form" transition:fade="{{ duration: 300 }}">
            <div class="close-button">
                <button class="close-button-inner" on:click={() => state = false}>

                    <svg fill="#333" class="button-icon-close" viewBox="0 0 329.26933 329"
                         xmlns="http://www.w3.org/2000/svg">
                        <path d="m194.800781 164.769531 128.210938-128.214843c8.34375-8.339844 8.34375-21.824219 0-30.164063-8.339844-8.339844-21.824219-8.339844-30.164063 0l-128.214844 128.214844-128.210937-128.214844c-8.34375-8.339844-21.824219-8.339844-30.164063 0-8.34375 8.339844-8.34375 21.824219 0 30.164063l128.210938 128.214843-128.210938 128.214844c-8.34375 8.339844-8.34375 21.824219 0 30.164063 4.15625 4.160156 9.621094 6.25 15.082032 6.25 5.460937 0 10.921875-2.089844 15.082031-6.25l128.210937-128.214844 128.214844 128.214844c4.160156 4.160156 9.621094 6.25 15.082032 6.25 5.460937 0 10.921874-2.089844 15.082031-6.25 8.34375-8.339844 8.34375-21.824219 0-30.164063zm0 0"/>
                    </svg>

                </button>
            </div>
            <div class="title">Заявка для добавления нового наименования места происхождения товара</div>


            <label class="label label__name">
                <div class="label-name">
                    Наименование места происхождения товара
                </div>
                <input bind:value={inputName} class="input input__name" type="text"/>
                {#if inputName !== ''}
                    <button class="clear-button" on:click={_ => inputName = ''}>
                        <svg class="clear-button-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                            <defs/>
                            <g id="expanded">
                                <path d="M267.31 256l80.9-80.9a8 8 0 10-11.32-11.3L256 244.68l-80.9-80.9a8 8 0 10-11.3 11.31l80.89 80.9-80.9 80.9a8 8 0 1011.32 11.3L256 267.32l80.9 80.9a7.98 7.98 0 0011.3 0 8 8 0 000-11.32L267.32 256z"/>
                                <path d="M256 59a196.36 196.36 0 01139.3 57.7A196.37 196.37 0 01453 256a196.37 196.37 0 01-57.7 139.3A196.37 196.37 0 01256 453a196.37 196.37 0 01-139.3-57.7A196.36 196.36 0 0159 256a196.37 196.37 0 0157.7-139.3A196.37 196.37 0 01256 59m0-16C138.36 43 43 138.36 43 256s95.36 213 213 213 213-95.36 213-213S373.64 43 256 43z"/>
                            </g>
                        </svg>
                    </button>
                {/if}
            </label>


            <label class="label label__name">
                <div class="label-name">
                    Указание товара
                </div>
<!--                <input bind:value={inputDescription} class="input input__name" type="text"/>-->
                <textarea form="new-nmpt-form" bind:value={inputDescription} class="input textarea input__description"></textarea>
                {#if inputDescription !== ''}
                    <button class="clear-button" on:click={_ => inputDescription = ''}>
                        <svg class="clear-button-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                            <defs/>
                            <g id="expanded">
                                <path d="M267.31 256l80.9-80.9a8 8 0 10-11.32-11.3L256 244.68l-80.9-80.9a8 8 0 10-11.3 11.31l80.89 80.9-80.9 80.9a8 8 0 1011.32 11.3L256 267.32l80.9 80.9a7.98 7.98 0 0011.3 0 8 8 0 000-11.32L267.32 256z"/>
                                <path d="M256 59a196.36 196.36 0 01139.3 57.7A196.37 196.37 0 01453 256a196.37 196.37 0 01-57.7 139.3A196.37 196.37 0 01256 453a196.37 196.37 0 01-139.3-57.7A196.36 196.36 0 0159 256a196.37 196.37 0 0157.7-139.3A196.37 196.37 0 01256 59m0-16C138.36 43 43 138.36 43 256s95.36 213 213 213 213-95.36 213-213S373.64 43 256 43z"/>
                            </g>
                        </svg>
                    </button>
                {/if}
            </label>


            <label class="label label__name">
                <div class="label-name">
                    Указание границ географического объекта:
                </div>
<!--                <input bind:value={inputGeo} class="input input__name" type="text"/>-->
                <textarea form="new-nmpt-form" bind:value={inputGeo} class="input textarea input__geo"></textarea>

                {#if inputGeo !== ''}
                    <button class="clear-button" on:click={_ => inputGeo = ''}>
                        <svg class="clear-button-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                            <defs/>
                            <g id="expanded">
                                <path d="M267.31 256l80.9-80.9a8 8 0 10-11.32-11.3L256 244.68l-80.9-80.9a8 8 0 10-11.3 11.31l80.89 80.9-80.9 80.9a8 8 0 1011.32 11.3L256 267.32l80.9 80.9a7.98 7.98 0 0011.3 0 8 8 0 000-11.32L267.32 256z"/>
                                <path d="M256 59a196.36 196.36 0 01139.3 57.7A196.37 196.37 0 01453 256a196.37 196.37 0 01-57.7 139.3A196.37 196.37 0 01256 453a196.37 196.37 0 01-139.3-57.7A196.36 196.36 0 0159 256a196.37 196.37 0 0157.7-139.3A196.37 196.37 0 01256 59m0-16C138.36 43 43 138.36 43 256s95.36 213 213 213 213-95.36 213-213S373.64 43 256 43z"/>
                            </g>
                        </svg>
                    </button>
                {/if}
            </label>


            <button class="submit-button" on:click={submit}>Просмотреть обработанные данные</button>


        </form>
    </div>

{/if}