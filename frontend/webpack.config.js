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
    mode: "development",
    devtool: "inline-source-map",
    devServer: {
        contentBase: path.join(__dirname, '../backend/static'),
        compress: false,
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
                    // HACK
                    publicPath: 'https://sfo2.digitaloceanspaces.com/timbrook/static',
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