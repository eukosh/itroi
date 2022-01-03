import lxml.etree

xml_file = lxml.etree.parse("/home/eukosh/Desktop/projects/Tryouts/answers_itroi/task5/task5.xml")
xml_validator = lxml.etree.XMLSchema(file="/home/eukosh/Desktop/projects/Tryouts/answers_itroi/task5/task5.xsd")

is_valid = xml_validator.validate(xml_file)

print(is_valid)
