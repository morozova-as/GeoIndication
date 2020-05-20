

<style>
    .container {
        display: grid;
        height: 100%;
        grid-template-columns: auto min-content;
    }

</style>

<div class="container">
    <slot name="map" class="map"/>
    <slot name="info-panel" class="info-panel"/>
    <slot name="finder" class="finder" />
    <slot name="form" class="form"/>
    <slot></slot>
</div>