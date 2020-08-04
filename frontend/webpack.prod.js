const { merge } = require('webpack-merge');
const common = require('./webpack.common.js');

module.exports = merge(common, {
    mode: 'production',
    module: {
        rules: [
            {
                test: /\.(jpg)$/,
                loader: 'file-loader',
                options: {
                    publicPath: 'https://sfo2.digitaloceanspaces.com/timbrook/static',
                },
            },
        ],
    },
});