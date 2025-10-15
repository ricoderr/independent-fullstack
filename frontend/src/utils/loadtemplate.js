export const loadTemplate = async (templatePath) => {
  const response = await fetch(templatePath);
  const templateText = await response.text();
  return templateText;
};
