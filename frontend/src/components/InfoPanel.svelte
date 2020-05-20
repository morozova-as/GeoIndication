<script>
    import { quintOut } from 'svelte/easing';
    import { fade } from 'svelte/transition';
    import { stateInfoPanel } from './store'


    let panel;

    function translate(node, params) {
        return {
            duration: params.duration || 400,
            easing: params.easing || quintOut,
            css: (t) => {
                return `width: ${330 * t}px; padding-left: ${15 * t}px; padding-right: ${15 * t}px`
            },
        };
    }

    const togglePanel = () => {
        stateInfoPanel.set(!$stateInfoPanel)
    }
</script>

<style>
    .right-panel {
		box-sizing: border-box;
		position: relative;
        overflow: hidden;
		height: 100vh;
		/*width: 350px;*/
		background: #dde9dd;
		box-shadow: 0 8px 20px rgba(68, 75, 91, 0.2);
		padding: 50px 15px 15px;
        z-index: 1;
        border-radius: 7px;
        display: flex;
        flex-direction: column;
	}

    .right-panel-scroll {
        display: grid;
		grid-template-rows: minmax(auto, min-content);
		grid-row-gap: 20px;
        grid-template-columns: 100%;

        max-height: 100%;
        width: 300px;

        overflow-y: scroll;
        overflow-x: hidden;
    }

    .right-panel-scroll::-webkit-scrollbar {
        display: none;
        width: 4px;
    }


    .right-panel-scroll::-webkit-scrollbar-thumb {
        background-color: darkgrey;
        outline: 1px solid slategrey;
        border-radius: 8px;
    }

    .toggle-button{

    }

    .toggle-button__panel {
        position: absolute;
        right: 20px;
        top: 20px;
        width: 20px;
        height: 20px;
    }

    .toggle-button__separate {
        position: fixed;
        top: 70px;
        right: 6px;
        width: 50px;
        height: 50px;
    }

    .toggle-button__separate .button {
        padding: 10px 10px 5px;
        background: #fff;
        border-radius: 4px;
        box-shadow: 0 8px 20px rgba(68, 75, 91, 0.2);
    }

    .toggle-button__separate .button:not(:disabled):active  {
        background: #f3f3f3;
        transform: scale(0.95);
    }

    .toggle-button__separate .button:hover {
        background: #f3f3f3;
    }

    .button {
        background: transparent;
        border: none;
        padding: 0;
        margin: 0;
        cursor: pointer;
    }

    .toggle-button__panel .button:not(:disabled):active {
        background: transparent;
        transform: scale(0.95);
    }

    .button-icon {
        height: 100%;
        width: 100%;
    }

    :global(.panel-title){
        position: sticky;
        top: 0;
        z-index: 1;
        background: #dde9dd;;
        padding-bottom: 20px;
        text-align: center;

        font-size: 18px;
        font-weight: 700;

        width: 300px;
    }

</style>

{#if $stateInfoPanel}
    <div class="right-panel" bind:this={panel} transition:translate="{{duration: 1000}}"
    on:introend={() => document.body.dispatchEvent(new Event('panel-opened'))}>
        <slot name="title"/>

        <div class="right-panel-scroll">
            <slot/>
        </div>

        <div class="toggle-button toggle-button__panel">
            <button class="button" on:click={togglePanel}>

                <svg  fill="#333" class="button-icon" viewBox="0 0 329.26933 329" xmlns="http://www.w3.org/2000/svg"><path d="m194.800781 164.769531 128.210938-128.214843c8.34375-8.339844 8.34375-21.824219 0-30.164063-8.339844-8.339844-21.824219-8.339844-30.164063 0l-128.214844 128.214844-128.210937-128.214844c-8.34375-8.339844-21.824219-8.339844-30.164063 0-8.34375 8.339844-8.34375 21.824219 0 30.164063l128.210938 128.214843-128.210938 128.214844c-8.34375 8.339844-8.34375 21.824219 0 30.164063 4.15625 4.160156 9.621094 6.25 15.082032 6.25 5.460937 0 10.921875-2.089844 15.082031-6.25l128.210937-128.214844 128.214844 128.214844c4.160156 4.160156 9.621094 6.25 15.082032 6.25 5.460937 0 10.921874-2.089844 15.082031-6.25 8.34375-8.339844 8.34375-21.824219 0-30.164063zm0 0"/></svg>

            </button>
        </div>
    </div>
{:else}
    <div class="toggle-button toggle-button__separate" out:fade="{{ duration: 2000 }}">
        <button class="button"  on:click={togglePanel}>

<svg class="button-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <defs/>
  <g fill="#333" fill-rule="evenodd" clip-rule="evenodd">
    <path d="M29 0H7a3 3 0 00-3 3v2H3a3 3 0 00-3 3v20a4 4 0 004 4h24a4 4 0 004-4V3a3 3 0 00-3-3zm1 28a2 2 0 01-2 2H4a2 2 0 01-2-2V8a1 1 0 011-1h1v20a1 1 0 102 0V3a1 1 0 011-1h22a1 1 0 011 1v25z"/>
    <path d="M19.5 13h8a.5.5 0 100-1h-8a.5.5 0 000 1zM19.5 10h8a.5.5 0 100-1h-8a.5.5 0 000 1zM19.5 7h8a.5.5 0 100-1h-8a.5.5 0 000 1zM16.5 27h-8a.5.5 0 000 1h8a.5.5 0 000-1zM16.5 24h-8a.5.5 0 000 1h8a.5.5 0 000-1zM16.5 21h-8a.5.5 0 000 1h8a.5.5 0 000-1zM27.5 27h-8a.5.5 0 000 1h8a.5.5 0 000-1zM27.5 24h-8a.5.5 0 000 1h8a.5.5 0 000-1zM27.5 21h-8a.5.5 0 000 1h8a.5.5 0 000-1zM27.5 15h-19a.5.5 0 000 1h19a.5.5 0 000-1zM27.5 18h-19a.5.5 0 000 1h19a.5.5 0 000-1zM9 13h7a1 1 0 001-1V5a1 1 0 00-1-1H9a1 1 0 00-1 1v7a1 1 0 001 1zm1-7h5v5h-5V6z"/>
  </g>
</svg>
        </button>
    </div>
{/if}