<script>
	import Map from './Map.svelte';
	import Facets from "./Facets.svelte";
	import MenuPanel from "./MenuPanel.svelte";
	import {define} from './utils'

	export let ready;

	import { nameFacet, typeFacet } from './store';
	import Polygons from "./Polygons.svelte";


</script>
<svelte:head>
	<script defer async
			src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBFs_K_cmnS4_L5s1tIwWbqr5wKlv-u2CY&callback=initMap">
	</script>
	<link href="https://fonts.googleapis.com/css2?family=Overpass:wght@300;600;700&display=swap" rel="stylesheet">
</svelte:head>

<style>
	:global(body, html) {
		padding: 0;
		margin: 0;
		font-family: 'Overpass', sans-serif;
	}


</style>


{ #if ready }
	<Map/>
	<MenuPanel>
		<Facets
				type="type"
				store={typeFacet}
				facetTitle='Type'
				request='http://localhost:8000/get_indications_classes/'
		/>
		<Facets
				facetTitle='Product'
				store={nameFacet}
				type="product"
				request='http://localhost:8000/get_indications_names/'
		/>
		<Polygons
				request='http://localhost:8000/get_polygons_by_facets/'
		/>
	</MenuPanel>
{ /if }