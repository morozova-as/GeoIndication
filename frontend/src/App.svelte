<script>
    import Map from './components/Map.svelte';
    import Facets from "./components/Facets.svelte";
    import MenuPanel from "./components/MenuPanel.svelte";

    export let ready;

    import {nameFacet, typeFacet} from './components/store';
    import Polygons from "./components/Polygons.svelte";
    import InfoPanel from "./components/InfoPanel.svelte";
    import Container from "./components/Container.svelte";
    import InfoBlock from "./components/InfoBlock.svelte";
    import Control from "./components/Control.svelte";
    import Alert from "./components/Alert.svelte";
    import ClickFinder from "./components/ClickFinder.svelte";
    import Loader from "./components/Loader.svelte";
    import ImgTooltip from "./components/ImgTooltip.svelte";
    import Form from "./components/Form.svelte";

    const { protocol, hostname } = window.location;

    const baseURL = `${protocol}//${hostname}:8000/`;

</script>

<svelte:head>
    <script defer async
            src="https://maps.googleapis.com/maps/api/js?key={process.env.MAP_API_KEY}&callback=initMap">
    </script>

    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@200;300;400;600;700&display=swap" rel="stylesheet">

<!--    <link href="https://fonts.googleapis.com/css2?family=Overpass:wght@300;600;700&display=swap" rel="stylesheet">-->


</svelte:head>

{ #if ready }

    <Control/>
    <Alert/>
    <Loader/>

    <MenuPanel>
        <Facets
                type="type"
                store={typeFacet}
                facetTitle='Тип'
                request={`${baseURL}get_indications_classes/`}
        />
        <Facets
                facetTitle='Название'
                store={nameFacet}
                type="product"
                isSearch
                isLetters
                isButtons
                request={`${baseURL}get_indications_names/`}
        />
        <Polygons
                request={`${baseURL}get_polygons_by_facets/`}
        />
    </MenuPanel>

    <Container>
        <div slot="map" style="display: contents">
            <Map/>
        </div>

        <div slot="info-panel" style="display: contents">
            <ImgTooltip />
            <InfoPanel>
                <div class="panel-title" slot="title">Выбранные наименования</div>
                <InfoBlock requestInfo={`${baseURL}get_info/`}/>
            </InfoPanel>
        </div>

        <div slot="finder" style="display: contents">
            <ClickFinder
                    requestUrl={`${baseURL}check_polygons/`}
            />
        </div>

<!--        <div slot="form" style="display: contents">-->
<!--            <Form requestGeoUrl={`${baseURL}define_geo_polygon/`} />-->
<!--        </div>-->

    </Container>
{ /if }