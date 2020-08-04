import React from 'react';
import { entrypointLoader } from '../utils/render';
import ProfileImage from '../static/profile.jpg';
import { Grid, Row, Col } from 'react-flexbox-grid';

const HomeEntrypoint = (props) => {
    return (
        <div style={{marginTop: "100px"}}>
            <Grid fluid>
                <Row middle="md" center="md">
                    <Col md={5}>
                        <img src={ProfileImage} width="100%" />
                    </Col>
                    <Col md={6}>
                        <h2>timbrook(dot)dev</h2>
                        <h6>Don't think about it too hard</h6>
                    </Col>
                </Row>
            </Grid>
        </div>
    );
}

entrypointLoader((props) => <HomeEntrypoint {...props} />);