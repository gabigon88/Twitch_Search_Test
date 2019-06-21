Feature: Search the specify keyword at Twitch

  Scenario Outline: Search right keyword
    Given I key <keyword> in search bar
    When I search the keyword
    Then the first result should be matched

  Examples: right keyword
    | keyword       | !notes        |
    | 餐餐自由配     | Streamer name |
    | Just Chatting | Category name |
  
  Scenario Outline: Search tag name
    Given I key <keyword> in search bar
    When I search the keyword
    Then the tag of first result should be matched

  Examples: tag keyword
    | keyword | !notes   |
    | 中文    | Tag name |

  Scenario Outline: Search no-matched keyword
    Given I key <keyword> in search bar
    When I search the keyword
    Then the first result should not be matched

  Examples: no-matched keyword
    | keyword | !notes          |
    | unirook | wrong keyword   |