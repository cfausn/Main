require_relative 'phonetic'
require 'test/unit'

class PhoneticTest < Test::Unit::TestCase

  def test_rit_to_phonetic
    assert_equal 'ROMEO INDIA TANGO', Phonetic.to_phonetic('RIT')
  end

  def test_line_rit_to_phonetic
    assert_equal 'ROMEO INDIA TANGO', Phonetic.translate('A2P RIT')
  end

  def test_line_software_to_phonetic
    assert_equal 'SIERRA OSCAR FOXTROT TANGO WHISKEY ALPHA ROMEO ECHO', Phonetic.translate('A2P Software')
  end 

  def test_line_engineering_to_phonetic
    assert_equal 'ECHO NOVEMBER GOLF INDIA NOVEMBER ECHO ECHO ROMEO INDIA NOVEMBER GOLF', Phonetic.translate('A2P engineering')
  end


  def test_line_RIT_from_phonetic
    assert_equal 'RIT', Phonetic.translate('P2A Romeo India Tango')
  end

  def test_line_COLIN_from_phonetic
    assert_equal 'COLIN', Phonetic.translate('P2A CHARLIE OSCAR LIMA INDIA NOVEMBER')
  end

  def test_line_SE_from_phonetic
    assert_equal 'SE', Phonetic.translate('p2a sierra echo')
  end
end
