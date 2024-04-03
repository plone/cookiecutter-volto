{% if not cookiecutter.noaddon -%}
const addons = ['{{ cookiecutter.npm_package_name }}'];
{% else -%}
const addons = [];
{% endif -%}
const theme = '';

module.exports = {
  addons,
  theme,
};
