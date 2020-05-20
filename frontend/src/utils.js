
export const LOCAL_STORAGE_NAMES = 'selected-names'
export const LOCAL_STORAGE_TYPES = 'selected-types'

export const setLocalFacets = (name, value) => {
    localStorage.setItem(name, JSON.stringify(value))
}

export const getLocalFacets = (name) => {
    return localStorage.getItem(name) ? JSON.parse(localStorage.getItem(name)) : [];
}



export const getBounds = (polys) => {
    let bounds = new google.maps.LatLngBounds();

    polys.forEach(poly => {
        let paths = poly.getPaths();
        let path;
        for (let i = 0; i < paths.getLength(); i++) {
            path = paths.getAt(i);
            for (let ii = 0; ii < path.getLength(); ii++) {
                bounds.extend(path.getAt(ii));
            }
        }
    })
    return bounds;
}