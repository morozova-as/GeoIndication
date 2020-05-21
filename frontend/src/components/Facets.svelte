<script>

    import {nameFacet, typeFacet} from './store'

    let facetFields;
    let filteredFacetFields;
    export let facetTitle;
    export let request;
    export let type;
    export let store;
    export let isSearch = false;
    export let isLetters = false;
    export let isButtons = false;
    let isPlaceholderUp = false;

    let valueSearch = '';
    let letters = [];
    let flag;

    let checkedFields = type === 'product' ? $nameFacet : $typeFacet;

    const fetchPromise = fetch(request);
    fetchPromise
            .then(response => response.json())
            .then(items => facetFields = items.map(e => e.trim()).sort())
            .then(() => filteredFacetFields = [...facetFields])
            .then( () => letters = Array.from(new Set(facetFields.map(e => toCapitalize(e)[0]))) )
            .then(() => letters = [...letters.filter(e => /[A-ZА-Я]/.test(e)), ...letters.filter(e => !/[A-ZА-Я]/.test(e))] )
            .catch(e => console.warn(e))

    store.subscribe(value => {
        checkedFields = value;
    })

    const toCapitalize = (value) => {
        const e = value.toLowerCase();
        return e.charAt(0).toUpperCase() + e.slice(1);
    }

    const onChangeValue = () => {
        store.updateData(checkedFields)
    }

    const turnOnAll = () => {
        checkedFields = facetFields;
        store.updateData(checkedFields)
    }

    const turnOffAll = () => {
        checkedFields = [];
        store.updateData(checkedFields)
    }


    const onInputFocus = () => {
        if (valueSearch.length === 0)
            isPlaceholderUp = true;
    }

    const onInputBlur = () => {
        if (valueSearch.length === 0)
            isPlaceholderUp = false;
    }

    const onSearchValueChange = (node, value) => {
        return {
            update(value) {
                filteredFacetFields = facetFields.filter(e => e.toLowerCase().includes(value.toLowerCase()))
            }
        }
    }


</script>

<style>
    .facet {
        background: #fff;
        padding: 0 20px 20px;
        /*max-height: 350px;*/
        border-radius: 8px;
        overflow: auto;
        box-shadow: 0 4px 6px 0 hsla(0, 0%, 0%, 0.2);
    }

    ::-webkit-scrollbar {
        width: 4px;
    }


    ::-webkit-scrollbar-thumb {
        background-color: #a9a9a9;
        outline: 1px solid #708090;
        border-radius: 8px;
    }

    .facet-title {
        font-size: 20px;
        line-height: 24px;
        font-weight: 600;
        position: sticky;
        top: 0;
        padding: 20px 0 5px;
        z-index: 2;
        background: #fff;
        border-bottom: 1px solid #000;
    }

    .facet-fields {
        /*margin-top: 10px;*/
        padding-top: 15px;
        display: flex;
        flex-direction: column;
    }

    .field {
        /*margin-bottom: 10px;*/


        border-radius: 4px;
        padding: 7px 5px;
    }

    .field:hover {
        background: #dadada26;
    }

    .field__hide {
        display: none;
    }

    .field__up {
        order: -1;
    }

    .field:last-child {
        margin-bottom: 0;
    }


    .field-input {
        display: none;
    }

    .field-label {
        display: block;
        position: relative;
        padding-left: 25px;
        cursor: pointer;
        font-size: 14px;
        line-height: 16px;
    }

    .field-label:focus {
        outline: 1px solid #b17e55;
        outline-offset: 5px;
    }

    .field-label:before {
        content: '';
        display: block;
        width: 14px;
        height: 14px;
        border: 1px solid #476c47;
        position: absolute;
        left: 0;
        opacity: .6;
        transition: all .12s, border-color .08s;
    }

    .field-input:checked + .field-label:before {
        width: 10px;
        top: -5px;
        left: 5px;
        border-radius: 0;
        opacity: 1;
        border-top-color: transparent;
        border-left-color: transparent;
        transform: rotate(45deg);
    }

    .letter {
        font-weight: 600;
        overflow: hidden;
        font-size: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #476c47;
        padding: 10px 0;
    }

    .letter.hide {
        display: none;
    }

    .letter:first-child {
        padding-top: 0;
    }

    .letter:before, .letter:after {
        content: '';
        display: inline-flex;
        height: 2px;
        background-color: #93b893;
        position: relative;
    }

    .letter:before {
        width: 20px;
        margin-right: 5px;
    }

    .letter:after {
        width: 180px;
        margin-left: 5px;
    }


    .container-input {
        display: flex;
        flex-direction: column;
        position: relative;
        width: 100%;
        padding-top: 10px;
        margin: 25px 0 20px;
    }

    .placeholder-input {
        transform-origin: 0 50%;
        transform: translateX(10px);
        padding-bottom: 3px;
        width: fit-content;
        font-size: 14px;

        display: flex;
        align-items: center;
        justify-content: center;
    }

    .placeholder-input.up {
        animation: MovePlaceholder 220ms both linear;
    }

    .placeholder-input.down {
        animation: ReturnPlaceholder 220ms both linear;
    }

    .input {
        width: 100%;
        background: transparent;
        font-size: 16px;
        height: 30px;
        outline: none !important;
        position: absolute;
        bottom: 0;
        margin: 0;
        border: 1px solid black;
        padding: 10px 10px;
    }

    .input:focus {
        background: #dadada26;
    }

    @keyframes MovePlaceholder {
        0% {
            transform: translateX(10px) translateY(0)
        }
        100% {
            transform: translateX(0) translateY(-30px) scale(0.75)
        }
    }

    @keyframes ReturnPlaceholder {
        0% {
            transform: translateX(0) translateY(-30px) scale(0.75)
        }
        100% {
            transform: translateX(10px) translateY(0)
        }
    }


    .close-button {
        position: absolute;
        top: 8px;
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

    .close-button:active {
        background: transparent;
        transform: scale(0.95);
    }


    .input-close {
        width: 100%;
    }

    .icon-find {
        height: 20px;
        margin-right: 7px;
        margin-bottom: 3px;
        transform: scale(-1, 1);

    }

    .facet-buttons {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }

    .facet-button {
        font-size: 14px;
        background: transparent;
        cursor: pointer;
        margin: 0;
    }

    .facet-button:hover {
        background: #dadada26;
    }

    .facet-button:focus {
    }

    .facet-button:active {
        outline: none;
        background: #dadada26;
        transform: scale(0.96);
    }

</style>


{#if facetFields && filteredFacetFields}
    <div class="facet">
        <div class="facet-title">
            {facetTitle}
        </div>

        {#if isSearch}
            <div class="container-input">
                <div class="placeholder-input" class:up={isPlaceholderUp} class:down={!isPlaceholderUp}>
                    <svg class="icon-find" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1009.99 1010">
                        <defs/>
                        <path fill="#5C524C"
                              d="M90.58 1010c-24.2 0-46.93-9.4-64.04-26.5A90.06 90.06 0 010 919.4a89.98 89.98 0 0126.54-64.06l183.13-183.13a89.98 89.98 0 0164.04-26.54 90.2 90.2 0 0164.08 26.5c35.3 35.37 35.29 92.86 0 128.16L154.66 983.5a90.06 90.06 0 01-64.08 26.5zm183.13-327.6c-14.38 0-27.9 5.6-38.07 15.78L52.51 881.31a53.5 53.5 0 00-15.78 38.1c0 14.38 5.6 27.93 15.78 38.12 20.34 20.33 55.8 20.33 76.18-.04l183.13-183.13a53.95 53.95 0 00-.02-76.18 53.44 53.44 0 00-38.09-15.78z"/>
                        <path fill="#5C524C"
                              d="M343.24 736.2a18.38 18.38 0 01-17.77-13.7 52.84 52.84 0 00-13.67-24.36c-6.52-6.49-14.72-11.08-24.33-13.63a18.35 18.35 0 01-8.28-30.74l58.74-58.74c3.66-3.7 8.7-5.67 13.9-5.38a18.5 18.5 0 0113.3 6.74 343.91 343.91 0 0048.48 48.46 18.48 18.48 0 016.72 13.3 18.41 18.41 0 01-5.36 13.92l-58.75 58.75a18.39 18.39 0 01-12.98 5.38zm-19.33-75.21c5.02 3.26 9.66 7 13.86 11.19a87.93 87.93 0 0111.24 13.88l26.03-26a381.38 381.38 0 01-25.11-25.11l-26.02 26.04z"/>
                        <path fill="#5C524C"
                              d="M630.5 759C421.22 759 251 588.76 251 379.5 251 170.24 421.22 0 630.5 0S1010 170.24 1010 379.5C1010 588.75 839.74 759 630.5 759zm0-722.27c-189 0-342.78 153.77-342.78 342.77 0 188.99 153.78 342.78 342.77 342.78 189 0 342.78-153.8 342.78-342.78 0-189-153.78-342.77-342.78-342.77z"/>
                        <path fill="#5C524C"
                              d="M431.87 379.82a18.35 18.35 0 01-18.37-18.36c0-129.62 105.43-235.07 235.03-235.07a18.35 18.35 0 110 36.73c-109.34 0-198.3 88.97-198.3 198.34a18.35 18.35 0 01-18.36 18.36z"/>
                    </svg>
                    ПОИСК
                </div>
                <label>
                    <input bind:value={valueSearch} class="input" on:focus={onInputFocus}
                           on:blur={onInputBlur} type="text" use:onSearchValueChange={valueSearch}/>
                    {#if valueSearch !== ''}
                        <button class="close-button" on:click={_ => valueSearch = ''}>
                            <svg class="input-close" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                                <defs/>
                                <g id="expanded">
                                    <path d="M267.31 256l80.9-80.9a8 8 0 10-11.32-11.3L256 244.68l-80.9-80.9a8 8 0 10-11.3 11.31l80.89 80.9-80.9 80.9a8 8 0 1011.32 11.3L256 267.32l80.9 80.9a7.98 7.98 0 0011.3 0 8 8 0 000-11.32L267.32 256z"/>
                                    <path d="M256 59a196.36 196.36 0 01139.3 57.7A196.37 196.37 0 01453 256a196.37 196.37 0 01-57.7 139.3A196.37 196.37 0 01256 453a196.37 196.37 0 01-139.3-57.7A196.36 196.36 0 0159 256a196.37 196.37 0 0157.7-139.3A196.37 196.37 0 01256 59m0-16C138.36 43 43 138.36 43 256s95.36 213 213 213 213-95.36 213-213S373.64 43 256 43z"/>
                                </g>
                            </svg>
                        </button>
                    {/if}
                </label>

            </div>

            <!--            <label>-->
            <!--                <input bind:value={valueSearch} on:input={changeSearchValue}>-->
            <!--            </label>-->
        {/if}

        {#if isButtons}
            <div class="facet-buttons">
                <button class="facet-button facet-button__plus" on:click={turnOnAll}>Выбрать все</button>
                <button class="facet-button facet-button__minus" on:click={turnOffAll}>Сбросить</button>
            </div>
        {/if}

        <div class="facet-fields">
            {#if isLetters}
                {#each letters as letter}
                    <div class="letter"
                         class:hide={filteredFacetFields.filter(e => toCapitalize(e[0]) === letter).length === 0}
                    >{!/[A-ZА-Я]/.test(letter) ? '#' : letter}</div>

                    {#each facetFields as name, index (facetFields.indexOf(name))}
                        {#if toCapitalize(name[0]) === letter}
                            <div class="field"
                                 class:field__hide={!filteredFacetFields.includes(name)}>
                                <!--                     class:field__up={checkedFields.includes(name)}-->
                                <!--                >-->
                                <input type=checkbox

                                       class="field-input"
                                       bind:group={checkedFields}
                                       on:change={onChangeValue}
                                       id={`${type}_${facetFields.indexOf(name)}`}
                                       value={name}>
                                <label for={`${type}_${facetFields.indexOf(name)}`} tabindex="-1"
                                       class="field-label">{toCapitalize(name)}</label>
                            </div>
                        {/if}
                    {/each}


                {/each}

            {:else}

                {#each facetFields as name, index (facetFields.indexOf(name))}
                    <div class="field"
                         class:field__hide={!filteredFacetFields.includes(name)}>
                        <!--                     class:field__up={checkedFields.includes(name)}-->
                        <!--                >-->
                        <input type=checkbox
                               class="field-input"
                               bind:group={checkedFields}
                               on:change={onChangeValue}
                               id={`${type}_${facetFields.indexOf(name)}`}
                               value={name}>
                        <label for={`${type}_${facetFields.indexOf(name)}`}
                               class="field-label">{toCapitalize(name)}</label>
                    </div>
                {/each}
            {/if}

        </div>

    </div>
{/if}