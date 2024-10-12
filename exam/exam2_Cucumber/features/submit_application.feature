Feature: Submit application for enterprise resumption

  Scenario: Fill and submit the application form
    Given I open the enterprise resumption application page
    When I select "连续生产/开工类企事业单位" in the "请选择贵单位情况" option group
    And I take a screenshot of the first page
    And I click the next page button
    And I fill in the following details on the second page
      | Field         | Content                           |
      | 申请日期       | The current year's New Year's Day |
      | 申请人         | 自动化                            |
      | 联系方式       | 1388888888                        |
    And I take a screenshot of the second page
    And I click the next page button again
    And I fill in the following details on the third page
      | Field                                                                 | Content          |
      | 报备单位                                                               | 测试公司         |
      | 在岗人数                                                               | 99              |
      | 报备日期                                                               | Current Date    |
      | 湖北籍员工、前往湖北以及与湖北人员密切接触的员工（人数）                   | 0               |
      | 单位负责人                                                             | 您的姓名         |
      | 联系方式                                                               | 13888888888     |
      | 疫情防控方案                                                           | 测试内容         |
    And I take a screenshot of the third page again
    When I click the submit button
    Then the form should be submitted successfully and take a screenshot of the result page
    And a HTML test report should be generated
