const addons = [{% if not cookiecutter.noaddon -%}'{{ cookiecutter.npm_package_name }}'{% endif -%}];
const theme = '';

module.exports = {
  addons,
  theme,
};
