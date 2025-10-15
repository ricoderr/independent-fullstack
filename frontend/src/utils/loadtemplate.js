const LoadTemplate = async (templatePath) => {
  const response = await fetch(templatePath);
  const templateText = await response.text();
  return templateText;
};

export default LoadTemplate; 