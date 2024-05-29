from lxml import etree
import os

class XMLRepository:

    def __init__(self, xml_file, root_element_name):
        self.xml_file = xml_file
        self.root_element_name = root_element_name
        if not os.path.exists(xml_file):
            self._create_empty_xml_file()
        self.tree = etree.parse(xml_file)
        self.root = self.tree.getroot()

    def _create_empty_xml_file(self):
        root = etree.Element(f'{self.root_element_name}s')
        tree = etree.ElementTree(root)
        with open(self.xml_file, 'wb') as f:
            f.write(etree.tostring(tree, pretty_print=True, xml_declaration=True, encoding='UTF-8'))

    def _save(self):
        with open(self.xml_file, 'wb') as f:
            f.write(etree.tostring(self.tree, pretty_print=True, xml_declaration=True, encoding='UTF-8'))

    def get_all(self):
        return self.root.findall(f".//{self.root_element_name}")

    def get_by_id(self, id):
        return self.root.find(f".//{self.root_element_name}[@id='{id}']")

    def add(self, item):
        self.root.append(item)
        self._save()

    def delete_by_id(self, id):
        element = self.get_by_id(id)
        if element is not None:
            self.root.remove(element)
            self._save()

    def update(self, item):
        id = item.attrib.get('id')
        self.delete_by_id(id)
        self.add(item)
