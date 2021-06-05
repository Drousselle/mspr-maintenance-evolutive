from django.db import models
import xml.etree.ElementTree as ET


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

    def action_fill_database(self):
        items = self.parse_xml(self.docfile)
        #self.save_to_csv(items)

    def parse_xml(self, xmlfile):
        tree = ET.parse(xmlfile)
        root = tree.getroot()
        return True
