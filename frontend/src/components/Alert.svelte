<script>
    import { alertState } from './store'
    import { fly } from 'svelte/transition';
	import { quintOut } from 'svelte/easing';


	alertState.subscribe(value => {
	    if (value === false)
	        return

        setTimeout(() => {
            alertState.set(false)
        }, 2000)
    })
</script>

<style>
    .alert {
        position: fixed;
        top: 20px;
        z-index: 2;

        left: calc(50% - 150px);

        width: 300px;

        text-align: center;
        background: rgba(0, 0, 0, 0.6);
        color: #ffffff;

        font-size: 14px;

        padding: 5px 10px;
        border-radius: 4px;


    }

</style>


{#if $alertState}
    <div class="alert" transition:fly="{{duration: 300, y: -100, opacity: 1, easing: quintOut}}">
        К сожалению, для данного товара нет информации о геграфическом местоположении.

    </div>
{/if}