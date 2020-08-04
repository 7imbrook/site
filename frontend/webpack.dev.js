const path = require('path');
const { merge } = require('webpack-merge');
const common = require('./webpack.common.js');

module.exports = merge(common, {
    mode: "development",
    devtool: "inline-source-map",
    devServer: {
        contentBase: path.join(__dirname, '../backend/static'),
        compress: false,
    },
    module: {
        rules: [
            {
                // Handle local file sourcing differently
                test: /\.(jpg)$/,
                loader: 'file-loader',
                options: {
                    publicPath: '/static',
                },
            },
        ],
    },
});