<script>
    import {imageGlobal} from './store'
    import {fly} from 'svelte/transition';
    import {quintOut} from 'svelte/easing';

    let state = false
    let imgUrl

    imageGlobal.subscribe(value => {

        if (value === '') {
            state = false;
            return;
        }

        imgUrl = value;
        state = true;
    })


</script>

<style>
    .wrapper-image {
        position: fixed;
        top: 10px;
        left: calc(50% - 150px);
        width: 300px;
        height: auto;
        padding: 10px;
        background: #fff;
        border-radius: 8px;
        max-height: 500px;
        object-fit: contain;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .image {
        max-width: 100%;
        /*height: 100%;*/
        max-height: 450px;

    }
</style>


{#if state}
    <div class="wrapper-image" transition:fly="{{duration: 300, y: -500, opacity: 1, easing: quintOut}}">
        <img class="image" src={imgUrl} alt="image of product" aria-hidden/>
    </div>
{/if}



