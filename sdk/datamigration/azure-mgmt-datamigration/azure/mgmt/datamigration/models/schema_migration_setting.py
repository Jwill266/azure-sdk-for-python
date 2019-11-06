# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SchemaMigrationSetting(Model):
    """Settings for migrating schema from source to target.

    :param schema_option: Option on how to migrate the schema. Possible values
     include: 'None', 'ExtractFromSource', 'UseStorageFile'
    :type schema_option: str or
     ~azure.mgmt.datamigration.models.SchemaMigrationOption
    :param file_id: Resource Identifier of a file resource containing the
     uploaded schema file
    :type file_id: str
    """

    _attribute_map = {
        'schema_option': {'key': 'schemaOption', 'type': 'str'},
        'file_id': {'key': 'fileId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SchemaMigrationSetting, self).__init__(**kwargs)
        self.schema_option = kwargs.get('schema_option', None)
        self.file_id = kwargs.get('file_id', None)