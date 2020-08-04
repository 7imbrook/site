import React from 'react';
import { entrypointLoader } from '../utils/render';
import ProfileImage from '../static/profile.jpg';
import { Grid, Row, Col } from 'react-flexbox-grid';

const style = {
    root: {
        marginTop: "20vh",
        fontFamily: "Hack, monospace"
    },
    span: {
        color: "rgb(162 162 175)"
    },
    img: {
        width: "100%"

    }
}

const HomeEntrypoint = (_props) => {
    return (
        <div style={style.root}>
            <Grid fluid>
                <Row middle="md" center="md">
                    <Col md={4}>
                        <img src={ProfileImage} style={style.img}/>
                    </Col>
                    <Col md={6}>
                        <h1>timbrook<span style={style.span}>(dot)</span>dev</h1>
                        <h5>Don't think about it too hard</h5>
                    </Col>
                </Row>
            </Grid>
        </div>
    );
}

entrypointLoader((props) => <HomeEntrypoint {...props} />);