<script>

	import { onMount } from 'svelte';
	import { mapGlobal } from './store';

	let container;
	let map;
	let zoom = 5;
    let center = { lat: 56.886, lng: 35.268 };



	onMount(async () => {
		map = new google.maps.Map(container, {
			zoom,
			center,
			mapTypeId: 'terrain',
			mapTypeControl: false
		});

		let styles = {
			'easy': [
				{
					featureType: 'administrative.country',
					elementType: 'labels',
					stylers: [
						{visibility: 'on'}
					]
				}, {
					featureType: 'administrative.country',
					elementType: 'geometry',
					stylers: [
						{visibility: 'on'},
						{weight: 1}
					]
				}
			]
		};

		map.set('styles', styles);

		mapGlobal.set(map);

	});


</script>

<style>
	.full-screen {
		width: 100%;
		height: 100%;
	}
</style>

<div class="full-screen" bind:this={ container }></div>