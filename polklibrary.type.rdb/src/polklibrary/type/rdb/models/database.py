from plone import api
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from zope import schema
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

resource_types = SimpleVocabulary([
    SimpleTerm(value=u'Art', title=u'Art'),
    SimpleTerm(value=u'Articles', title=u'Articles'),
    SimpleTerm(value=u'Books', title=u'Books'),
    SimpleTerm(value=u'DVD/VHS', title=u'DVD/VHS'),
    SimpleTerm(value=u'eBooks', title=u'eBooks'),
    SimpleTerm(value=u'Images', title=u'Images'),
    SimpleTerm(value=u'Graphic Novels', title=u'Graphic Novels'),
    SimpleTerm(value=u'Journals', title=u'Journals'),
    SimpleTerm(value=u'Magazines', title=u'Magazines'),
    SimpleTerm(value=u'Music', title=u'Music'),
    SimpleTerm(value=u'Newspaper Resources', title=u'Newspapers'),
    SimpleTerm(value=u'Primary Source Resources', title=u'Primary Sources'),
    SimpleTerm(value=u'Reference and Background Resources', title=u'Reference and Background'),
    SimpleTerm(value=u'Sheet Music', title=u'Sheet Music'),
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
        
    location = schema.TextLine(
            title=u"Tutorial Link",
            required=False,
            default=u"",
        )

        
        