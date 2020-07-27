import ReactDOM from 'react-dom';

export function entrypointLoader(renderRoot) {
    ReactDOM.render(renderRoot(window.initialPageData), document.getElementById('react-root'));
}