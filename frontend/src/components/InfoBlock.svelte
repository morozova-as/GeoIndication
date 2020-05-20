<script>

    import {renderedKeysGlobal} from './store'
    import InfoBlockItem from "./InfoBlockItem.svelte";


    export let requestInfo;
    let renderedKeys;
    let infoForRender;

    let flag = false;

    renderedKeysGlobal.subscribe(value => {
        renderedKeys = Object.keys($renderedKeysGlobal);

        const fetchPromise = fetch(requestInfo, {
            method: 'POST',
            body: JSON.stringify(renderedKeys)
        });

        fetchPromise
                .then(response => response.json())
                .then(items => infoForRender = items)
                .then(() => {
                    if (Object.keys(infoForRender).length !== 0)
                        flag = true
                })
                .catch(e => {
                    console.warn(e);
                })
    })
</script>


<style>

    .alert {
        text-align: center;
        font-size: 16px;
        padding: 20px 50px;
        background-color: #ffffff8f;
    }

</style>

{#if flag && infoForRender && Object.keys(infoForRender).length !== 0}
    {#each renderedKeys as key, index (key)}
        <InfoBlockItem key={key}
                       manufacturers={infoForRender[key]}
        />
    {/each}

{:else}
    <div class="alert">
        ¯\_(ツ)_/¯
        <br/>
        <br/>
        Не найдено наименований для выбранных фильтров
    </div>
{/if}