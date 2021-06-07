from pages.registration import RegistrationPage

validate_input_field = RegistrationPage.validate_input_field
validate_readonly_input_field = RegistrationPage.validate_readonly_input_field


def test_registration_form(landing_page):
    registration_page_title = 'Limit kredytowy na wyciągnięcie ręki!';

    registration_progress_bar_title = 'Dane kontaktowe:\nKrok 1 z 4'

    amount_calculator_title = 'Określ wartość\nmiesięcznej raty\nzł'

    name_input_field_tip_text = 'Zgodne z dokumentem tożsamości (Jan Maciej)'

    surname_input_field_tip_text = 'Zgodne z dokumentem tożsamości'

    doc_nr_input_field_tip_text = 'Zgodne z dokumentem tożsamości'

    phone_input_field_tip_text = 'Nie otrzymałeś SMS? Wyslij ponownie'

    ## Preconditions
    # User navigates to the website - 'vialet.pl'.
    landing_page.open()

    # User navigates to the registration page by clicking the button 'Wnioskuj o limit'.
    registration_page = landing_page.click_register()

    # User closes the notification pop-up.
    registration_page.close_notification_popup()

    ## Main steps
    # Validate that registration page title is present.
    assert registration_page.is_title_visible() == True
    assert registration_page.get_title_text() == registration_page_title

    # Validate that the 'Registration steps' progress bar is present.
    assert registration_page.is_registration_progress_bar_visible() == True

    # Validate that 'Registration steps' progress title is present.
    assert registration_page.is_registration_progress_bar_title_visible() == True
    assert registration_page.get_registration_progress_bar_title_text() == registration_progress_bar_title

    # Validate that the open 'Amount calculator toolbar' title and button are present.
    assert registration_page.is_amount_calculator_button_visible() == True
    assert registration_page.is_amount_calculator_title_visible() == True
    assert registration_page.get_amount_calculator_title__text() == amount_calculator_title

    # Validate that input fields are present for following attributes: name/surname/NIN/IDN/email/phone number.
    # Validate that placeholder texts are present for all empty input fields.
    validate_input_field(registration_page.get_name_input_field(), "Jan")
    validate_input_field(registration_page.get_surname_input_field(), "Kowalski")
    validate_input_field(registration_page.get_nin_input_field(), "70082742729")
    validate_input_field(registration_page.get_idn_input_field(), "AXY312332")
    validate_input_field(registration_page.get_email_input_field(), "email@email.pl")
    validate_input_field(registration_page.get_phone_input_field(), "660573996")

    # Validate that DDM is present for the following attribute: identification document type.
    registration_page.validate_document_type_drop_down("Dowód osobisty", ["Dowód osobisty", "Paszport"])

    # Validate that prefilled non-editable fields are present for following attributes: home country / phone number country code.
    validate_readonly_input_field(registration_page.get_country_input_field(), "Polska")
    validate_readonly_input_field(registration_page.get_phone_prefix_input_field(), "+48")

    # Validate that tooltips are present for fields: NIN / IDN.
    registration_page.validate_registration_page_tooltips()

    # Validate that tips are present for fields: name/ surname / IDN/ phone.
    registration_page.validate_input_field_tip(name_input_field_tip_text)
    registration_page.validate_input_field_tip(surname_input_field_tip_text)
    registration_page.validate_input_field_tip(doc_nr_input_field_tip_text)
    registration_page.validate_input_field_tip(phone_input_field_tip_text)

    # Validate that 'submit form and send verification SMS' button is present.
    assert registration_page.is_resend_sms_button_visible() == True
