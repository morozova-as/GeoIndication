<script>
    import { quintOut } from 'svelte/easing';
    import { fade } from 'svelte/transition';

    export let state = true;

    function translate(node, params) {
        return {
            duration: params.duration || 400,
            easing: params.easing || quintOut,
            css: (t, u) => {
                return `transform: translateX(-${100 * u}%)`
            }
        };
    }

    const togglePanel = () => {
        state = !state;
    }
</script>

<style>
    .left-panel {
		box-sizing: border-box;
		position: fixed;
		left: 0;
		top: 0;
		height: 100vh;
		width: 270px;
		background: #dde9dd;
		box-shadow: 0 8px 20px rgba(68, 75, 91, 0.2);
		padding: 50px 15px;
        z-index: 3;
        border-radius: 7px;

		display: grid;
		grid-template-rows: minmax(auto, min-content);
		grid-row-gap: 20px;
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
        top: 20px;
        left: 20px;
        width: 50px;
        height: 50px;
        z-index: 2;
    }

    .toggle-button__separate .button {
        padding: 10px 10px 5px;
        background: #fff;
        border-radius: 4px;
        box-shadow: 0 8px 20px rgba(68, 75, 91, 0.2);
    }

    .toggle-button__separate .button:not(:disabled):active  {
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

    .toggle-button__panel .button:not(:disabled):active {
        background: transparent;
        transform: scale(0.95);
    }

    .button-icon {
        height: 100%;
        width: 100%;
    }

</style>

{#if state}
    <div class="left-panel" transition:translate="{{duration: 1000}}">
        <slot/>
        <div class="toggle-button toggle-button__panel">
            <button class="button" on:click={togglePanel}>

                <svg fill="#333" class="button-icon" viewBox="0 0 329.26933 329" xmlns="http://www.w3.org/2000/svg"><path d="m194.800781 164.769531 128.210938-128.214843c8.34375-8.339844 8.34375-21.824219 0-30.164063-8.339844-8.339844-21.824219-8.339844-30.164063 0l-128.214844 128.214844-128.210937-128.214844c-8.34375-8.339844-21.824219-8.339844-30.164063 0-8.34375 8.339844-8.34375 21.824219 0 30.164063l128.210938 128.214843-128.210938 128.214844c-8.34375 8.339844-8.34375 21.824219 0 30.164063 4.15625 4.160156 9.621094 6.25 15.082032 6.25 5.460937 0 10.921875-2.089844 15.082031-6.25l128.210937-128.214844 128.214844 128.214844c4.160156 4.160156 9.621094 6.25 15.082032 6.25 5.460937 0 10.921874-2.089844 15.082031-6.25 8.34375-8.339844 8.34375-21.824219 0-30.164063zm0 0"/></svg>

            </button>
        </div>
    </div>
{:else}
    <div class="toggle-button toggle-button__separate" out:fade="{{ duration: 2000 }}">
        <button class="button"  on:click={togglePanel}>

<svg fill="#333" class="button-icon" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="m208 512c-2.582031 0-5.183594-.617188-7.550781-1.898438-5.207031-2.773437-8.449219-8.214843-8.449219-14.101562v-205.226562c0-7.464844-3.136719-14.636719-8.640625-19.667969l-171.261719-156.867188c-7.703125-7.082031-12.097656-17.109375-12.097656-27.519531v-49.386719c0-20.585937 16.746094-37.332031 37.332031-37.332031h437.335938c20.585937 0 37.332031 16.746094 37.332031 37.332031v49.386719c0 10.410156-4.394531 20.4375-12.074219 27.519531l-171.242187 156.886719c-5.546875 5.011719-8.683594 12.183594-8.683594 19.648438v129.792968c0 12.5-6.207031 24.125-16.617188 31.058594l-86.507812 57.664062c-2.667969 1.816407-5.761719 2.710938-8.875 2.710938zm-170.667969-480c-2.941406 0-5.332031 2.390625-5.332031 5.332031v49.386719c0 1.496094.640625 2.925781 1.75 3.949219l171.199219 156.839843c12.097656 11.09375 19.050781 26.859376 19.050781 43.265626v175.316406l61.632812-41.085938c1.472657-.984375 2.367188-2.648437 2.367188-4.4375v-129.792968c0-16.425782 6.933594-32.191407 19.070312-43.265626l171.203126-156.863281c1.085937-1 1.726562-2.429687 1.726562-3.925781v-49.386719c0-2.941406-2.390625-5.332031-5.332031-5.332031zm0 0"/></svg>
        </button>
    </div>
{/if}