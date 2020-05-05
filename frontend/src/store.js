import { writable } from 'svelte/store';
import { derived } from 'svelte/store';



function createNameFacet() {
	const { subscribe, set, update } = writable([]);

	return {
		subscribe,
        updateData: (arr) => {
		    update(curr => {
		        return arr
		        // const additional = arr.filter(e => !curr.includes(e))
                // if (additional)
                //     return [...curr, additional]
            })
        }
	};
}


function createTypeFacet() {
	const { subscribe, set, update } = writable([]);

	return {
		subscribe,
        updateData: (arr) => {
		    update(curr => {
		        return arr
            })
        }
	};
}


function createRenderedKeys() {
	const { subscribe, set, update } = writable({});

	return {
		subscribe,
		addKey: (data) => {
			update(currData => {
				return {...currData, ...data}
			})
		},
		deleteKey: (key) => {
			update(currData => {
				return Object.keys(currData)
					.filter(e => e !== key)
					.reduce((obj, key) => {
						return {...obj, [key]: currData[key]}
					}, {});
			})
		}
	}
}



export const nameFacet = createNameFacet();
export const typeFacet = createTypeFacet();
export const mapGlobal = writable(null);
export const renderedKeysGlobal = createRenderedKeys();


// export const polygons = derived(
//     [nameFacet, typeFacet],
//     ([$nameFacet, $typeFacet]) => {
//         console.log($nameFacet, $typeFacet)
//     }
//     );