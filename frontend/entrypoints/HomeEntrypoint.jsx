import React from 'react';
import { entrypointLoader } from '../utils/render';
import { Container, Row, Col } from 'react-bootstrap';

const HomeEntrypoint = (props) => {
    return (<Container>
        <Row className="justify-content-md-center">
            <Col md="auto" style={{
                marginTop: 40
            }}>
                Welcome to Timbrook.tech (dev site).
            </Col>
        </Row>
    </Container>);
}

entrypointLoader((props) => <HomeEntrypoint {...props} />);