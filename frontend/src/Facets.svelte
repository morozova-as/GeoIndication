<script>
    import { beforeUpdate } from 'svelte';
    import { getCsrfToken, define } from './utils'

    let facetFields;
    export let facetTitle;
    export let request;
    export let type;
    export let store;

    let checkedFields = [];

    const fetchPromise = fetch(request);
    fetchPromise
            .then(response => response.json())
            .then(items => facetFields = items)


    const toCapitalize = (value) => {
        const e = value.toLowerCase();
        return e.charAt(0).toUpperCase() + e.slice(1);
    }


    const onChangeValue = () => {
        // console.log(checkedFields)
        store.updateData(checkedFields)
    }

    // $: {
    //
    //     console.log(checkedFields)
    // }

</script>

<style>
    .facet {
        background: #fff;
        padding: 0 20px 20px;
        max-height: 300px;
        border-radius: 8px;
        overflow: auto;
        box-shadow: 0 8px 20px rgba(68, 75, 91, 0.2);
    }

    ::-webkit-scrollbar {
        width: 4px;
    }


    ::-webkit-scrollbar-thumb {
        background-color: darkgrey;
        outline: 1px solid slategrey;
        border-radius: 8px;
    }

    .facet-title {
        font-size: 24px;
        line-height: 28px;
        font-weight: bold;
        position: sticky;
        top: 0;
        padding: 20px 0;
        z-index: 2;
        background: #fff;
    }

    .facet-fields {
        margin-top: 2px;
    }

    .field {
        margin-bottom: 10px;
    }
    .field:last-child { margin-bottom: 0; }


    .field-input { display: none; }

    .field-label {
        display: block;
        position: relative;
        padding-left: 35px;
        cursor: pointer;
        font-size: 20px;
        line-height: 24px;
    }

    .field-label:before {
        content: '';
        display: block;
        width: 20px;
        height: 20px;
        border: 1px solid #8d9588;
        position: absolute;
        left: 0;
        top: -2px;
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

</style>


{#if facetFields}
    <div class="facet">
        <div class="facet-title">
            {facetTitle}
        </div>

        <div class="facet-fields">
            {#each facetFields as name, index (`${type}_${index}`)}
                <div class="field">
                    <input type=checkbox
                           class="field-input"
                           bind:group={checkedFields}
                           on:change={onChangeValue}
                           id={`${type}_${index}`}
                           value={name}>
                    <label for={`${type}_${index}`}
                            class="field-label">{toCapitalize(name)}</label>
                </div>
            {/each}
        </div>

    </div>
{/if}