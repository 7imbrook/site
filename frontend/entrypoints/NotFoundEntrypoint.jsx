import React from 'react';
import { entrypointLoader } from '../utils/render';

const NotFoundEntrypoint = (_props) => {
    return <div>I don't know that one</div>
}

entrypointLoader((props) => <NotFoundEntrypoint {...props} />);