const getTokenColors = (tokens) => {
    const count = tokens.length;
    const color_range = ["#c00", "#0c0", "#00c", "#c0c","#0cc"];
    const coloredTokens = [];

    for (let i = 0; i < count; i++) {
        const style = `background-color: ${color_range[i % color_range.length]}`;
        coloredTokens.push([tokens[i], style]);
    }

    return coloredTokens;
}

module.exports = {
    getTokenColors
}