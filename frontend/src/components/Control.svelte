<script>

    import { nameFacet, typeFacet } from './store'
    import { setLocalFacets, LOCAL_STORAGE_NAMES, LOCAL_STORAGE_TYPES } from '../utils'

    nameFacet.subscribe(value => {
        setLocalFacets(LOCAL_STORAGE_NAMES, value);
    })

    typeFacet.subscribe(value => {
        setLocalFacets(LOCAL_STORAGE_TYPES, value);
    })
</script>