import React from 'react';
import { entrypointLoader } from '../utils/render';
import ProfileImage from '../static/profile.jpg';
import { Grid, Row, Col } from 'react-flexbox-grid';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faTwitter, faGithub } from '@fortawesome/free-brands-svg-icons'

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

    },
    links: {
        color: "rgb(162 162 175)",
        marginRight: "4px",
        marginLeft: "4px",
    }
}

const HomeEntrypoint = (props) => {
    return (
        <div style={style.root}>
            <Grid fluid>
                <Row middle="md" center="md">
                    <Col md={4}>
                        <img src={ProfileImage} style={style.img}/>
                    </Col>
                    <Col md={6}>
                        <h1>timbrook<span style={style.span}>(dot)</span>dev</h1>
                        <h5>{props.tagline}</h5>
                        <a style={style.links} href={'https://twitter.com/7imbrook'}><FontAwesomeIcon icon={faTwitter} /></a>
                        <a style={style.links} href={'https://github.com/7imbrook'}><FontAwesomeIcon icon={faGithub} /></a>
                    </Col>
                </Row>
            </Grid>
        </div>
    );
}

entrypointLoader((props) => <HomeEntrypoint {...props} />);