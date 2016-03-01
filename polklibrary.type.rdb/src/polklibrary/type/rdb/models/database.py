from plone import api
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from zope import schema
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

resource_types = SimpleVocabulary([
    SimpleTerm(value=u'Articles', title=u'Articles'),
    SimpleTerm(value=u'Books', title=u'Books'),
    SimpleTerm(value=u'Journals', title=u'Journals'),
    SimpleTerm(value=u'Newspaper Resources', title=u'Newspaper Resources'),
    SimpleTerm(value=u'Primary Source Resources', title=u'Primary Source Resources'),
    SimpleTerm(value=u'Reference and Background Resources', title=u'Reference and Background Resources'),
    SimpleTerm(value=u'Streaming Video', title=u'Streaming Video'),
])

message_types = SimpleVocabulary([
    SimpleTerm(value=u'Warning', title=u'Warning'),
    SimpleTerm(value=u'Trial', title=u'Trial'),
])


class IDatabase(model.Schema):

    title = schema.TextLine(
            title=u"Title",
            required=True,
        )

    description = schema.Text(
            title=u"Description",
            required=True,
        )
        
    getRemoteUrl = schema.TextLine(
            title=u"URL (Add proxy if required here)",
            required=True,
        )
       
    resources = schema.List(
            title=u"Resources available",
            required=False,
            value_type=schema.Choice(source=resource_types),
        )
        
    activated = schema.Choice(
            title=u"Turn on message",
            source=message_types,
            required=False,
        )
        
    message = RichText(
            title=u"Message",
            default_mime_type='text/structured',
            required=False,
            default=u"",
        )
        
        

        
        