const path = require('path');
const webpack = require('webpack');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const CopyPlugin = require('copy-webpack-plugin');


module.exports = {
    entry: {
        Home: './entrypoints/HomeEntrypoint.jsx',
        NotFound: './entrypoints/NotFoundEntrypoint.jsx',
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
                test: /\.css$/,
                loader: 'style-loader!css-loader',
                include: /flexboxgrid/
            }
        ],
    },
    plugins: [
        new webpack.ProgressPlugin(),
        new CleanWebpackPlugin(),
        new CopyPlugin({
            patterns: [
                { from: 'favicon', to: '' },
            ],
        }),
    ]
};