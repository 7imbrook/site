import React from 'react';
import { entrypointLoader } from '../utils/render';

const HomeEntrypoint = (props) => {
    return <h1>Hello! {JSON.stringify(props)}</h1>;
}

entrypointLoader((props) => <HomeEntrypoint {...props} />);