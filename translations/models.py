from i18n_model.models import I18nModel


class HomePageTranslation(I18nModel):

    class Meta:
        source_model = 'demo.HomePage'
        translation_fields = ('title', 'body')
