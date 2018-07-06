from collections import OrderedDict

from django.utils import encoding, six

from rest_framework import renderers as restRenderers
from rest_framework_json_api.renderers import JSONRenderer
from rest_framework import relations
from rest_framework.settings import api_settings
from rest_framework_json_api import utils


class CustomRenderer(restRenderers.JSONRenderer):

    def render(self, data, *args, **kwargs):
        if not data.get('errors', None):
            data = {'result': {'code': 200, 'message': 'Success'},
                    'data': data}
        return super(CustomRenderer, self).render(data, *args, **kwargs)


class JSONRendererCustom(JSONRenderer):
    @classmethod
    def build_json_resource_obj(cls, fields, resource, resource_instance, resource_name,
                                force_type_resolution=False):
        # Determine type from the instance if the underlying model is polymorphic
        if force_type_resolution:
            resource_name = utils.get_resource_type_from_instance(resource_instance)
        resource_data = [
            ('type', resource_name),
            # ('id', encoding.force_text(resource_instance.pk) if resource_instance else None),
            ('attributes', cls.extract_attributes(fields, resource)),
        ]
        relationships = cls.extract_relationships(fields, resource, resource_instance)
        if relationships:
            resource_data.append(('relationships', relationships))
        # Add 'self' link if field is present and valid
        if api_settings.URL_FIELD_NAME in resource and \
                isinstance(fields[api_settings.URL_FIELD_NAME], relations.RelatedField):
            resource_data.append(('links', {'self': resource[api_settings.URL_FIELD_NAME]}))
        return OrderedDict(resource_data)


class JSONRenderer(JSONRenderer):
    @classmethod
    def extract_attributes(cls, fields, resource):
        data = OrderedDict()
        for field_name, field in six.iteritems(fields):
            # ID is always provided in the root of JSON API so remove it from attributes
            if field_name == 'id':
                continue
            # don't output a key for write only fields
            if fields[field_name].write_only:
                continue
            # Skip fields with relations
            # if isinstance(
            #         field, (relations.RelatedField, relations.ManyRelatedField, BaseSerializer)
            # ):
            #     continue

            # Skip read_only attribute fields when `resource` is an empty
            # serializer. Prevents the "Raw Data" form of the browsable API
            # from rendering `"foo": null` for read only fields
            try:
                resource[field_name]
            except KeyError:
                if fields[field_name].read_only:
                    continue

            data.update({
                field_name: resource.get(field_name)
            })

        return utils.format_keys(data)

    @classmethod
    def build_json_resource_obj(cls, fields, resource, resource_instance, resource_name,
                                force_type_resolution=False):
        # Determine type from the instance if the underlying model is polymorphic
        if force_type_resolution:
            resource_name = utils.get_resource_type_from_instance(resource_instance)

        # Hide id if the resource_name is 'User'
        resource_data = [
            ('type', resource_name),
            ('id', encoding.force_text(resource_instance.pk) if resource_instance and resource_name != 'User' else None),
            ('attributes', cls.extract_attributes(fields, resource)),
        ]
        # relationships = cls.extract_relationships(fields, resource, resource_instance)
        # if relationships:
        #     resource_data.append(('relationships', relationships))
        # Add 'self' link if field is present and valid
        if api_settings.URL_FIELD_NAME in resource and \
                isinstance(fields[api_settings.URL_FIELD_NAME], relations.RelatedField):
            resource_data.append(('links', {'self': resource[api_settings.URL_FIELD_NAME]}))
        return OrderedDict(resource_data)
