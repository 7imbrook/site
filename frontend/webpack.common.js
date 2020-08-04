const path = require('path');
const webpack = require('webpack');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');

module.exports = {
    entry: {
        Home: './entrypoints/HomeEntrypoint.jsx',
    },
    output: {
        path: path.resolve(__dirname, '../backend/static'),
        filename: '[name].entrypoint.js'
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                loader: 'babel-loader',
            },
            {
                test: /\.(jpg)$/,
                loader: 'file-loader',
                options: {
                    publicPath: '/static',
                },
            },
            {
                test: /\.css$/,
                loader: 'style-loader!css-loader',
                include: /flexboxgrid/
            }
        ],
    },
    plugins: [
        new webpack.ProgressPlugin(),
        new CleanWebpackPlugin(),
    ]
};