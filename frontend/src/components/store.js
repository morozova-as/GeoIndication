import { writable } from 'svelte/store';
import { derived } from 'svelte/store';
import { getLocalFacets, LOCAL_STORAGE_TYPES, LOCAL_STORAGE_NAMES } from "../utils";


function createNameFacet() {
	const { subscribe, set, update } = writable(getLocalFacets(LOCAL_STORAGE_NAMES));

	return {
		subscribe,
        updateData: (arr) => {
		    update(curr => {
		    	isInitState.set(false);

				const isAdd = arr.filter(e => !curr.includes(e))
				const isDel = curr.filter(e => !arr.includes(e))
				if (isAdd.length !== 0)
					globalAction.set(1)
				else if (isDel.length !== 0)
					globalAction.set(-1)
				else
					globalAction.set(0)

		        return arr
		        // const additional = arr.filter(e => !curr.includes(e))
                // if (additional)
                //     return [...curr, additional]
            })
        },
		addData: (arr) => {
			update(curr => {
				return [...curr, ...arr]
			})
		}
	};
}


function createTypeFacet() {
	const { subscribe, set, update } = writable(getLocalFacets(LOCAL_STORAGE_TYPES));

	return {
		subscribe,
        updateData: (arr) => {
		    update(curr => {
		    	isInitState.set(false);


		    	const isAdd = arr.filter(e => !curr.includes(e))
				const isDel = curr.filter(e => !arr.includes(e))
				if (isAdd.length !== 0)
					globalAction.set(1)
				else if (isDel.length !== 0)
					globalAction.set(-1)
				else
					globalAction.set(0)
		        return arr
            })
        }
	};
}


function createRenderedKeys() {
	const { subscribe, set, update } = writable({});

	return {
		subscribe,
		addEmptyData: (key) => {
			update(currData => {
				const newObj = { };
				newObj[key] = {};
				if (!(key in currData)) {
					return {...currData, ...newObj}
				}
				return currData
			})
		},
		addPoly: (key, idItem, data) => {
			update(currData => {
				const newObj = { };
				newObj[idItem] = data;

				if (key in currData) {
					currData[key]['poly'] = {...currData[key]['poly'], ...newObj}
				} else {
					currData[key] = { ...currData[key], 'poly': newObj }

				}

				return currData
			})
		},
		addCentroid: (key, value) => {
			update(currData => {

				currData[key]['centroid'] = value;

				return currData
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
		},
		deleteKeys: (keys) => {
			update(currData => {
				return Object.keys(currData)
					.filter( e => !keys.includes(e) )
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
export const globalAction = writable(1);

export const stateInfoPanel = writable(false);

export const alertState = writable(false);
export const isInitState = writable(true);

export const loadingState = writable(false);

export const imageGlobal = writable('');




// export const polygons = derived(
//     [nameFacet, typeFacet],
//     ([$nameFacet, $typeFacet]) => {
//         console.log($nameFacet, $typeFacet)
//     }
//     );