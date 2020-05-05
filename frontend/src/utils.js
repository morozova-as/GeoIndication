export const CorsCookieName = 'csrftoken';
export const corsDataName = 'csrfmiddlewaretoken';

export function getCookie(name) {
    var matches = document.cookie.match(new RegExp(
        "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ))
    return matches ? decodeURIComponent(matches[1]) : undefined
}

function setCookie(name, value, props) {
    props = props || {};
    var exp = props.expires;
    if (typeof exp == "number" && exp) {
        var d = new Date();
        d.setTime(d.getTime() + exp * 1000);
        exp = props.expires = d;
    }

    if (exp && exp.toUTCString) {
        props.expires = exp.toUTCString();
    }

    value = encodeURIComponent(value);
    var updatedCookie = name + "=" + value;

    for (var propName in props) {
        updatedCookie += "; " + propName;
        var propValue = props[propName];
        if (propValue !== true) {
            updatedCookie += "=" + propValue;
        }
    }

    document.cookie = updatedCookie;

}

export function deleteCookie(name) {
    setCookie(name, null, {expires: -1})
}





export function define() {
    return fetchCsrfToken()
        .then(res => res.json())
        .then(json => {
            console.log(json)
            if (json.csrfToken) {
                setCsrfToken(json.csrfToken)
                setCookie('csrftoken', json.csrfToken)
                console.log('setted')
            }
        })
        .catch(err => console.log(err))
}


function fetchCsrfToken() {
    return fetch('http://localhost:8000/csrf/',
        {method: "GET"})
}


function getToken() {
    return localStorage.getItem('token');
}

export function getCsrfToken() {
    return localStorage.getItem('csrfToken');
}

function setCsrfToken(token) {
    localStorage.setItem('csrfToken', token)
}