
context('Home Page', () => {

  before('Login', () => {
    // log in only once before any of the tests run.
    cy.visit('http://127.0.0.1:8000/')

    cy.get('#username')
      .type('test', { delay: 100 })
      .should('have.value', 'test')

    cy.get('#password')
      .type('tanuki404', { delay: 100 })
      .should('have.value', 'tanuki404')

    cy.get('.userinfo')
      .find('form').submit()

    cy.url().should('eq', 'http://127.0.0.1:8000/home/')
    cy.get('#budget1').click()
    cy.url().should('eq', 'http://127.0.0.1:8000/budget/')
  })

  beforeEach(() => {
    // before each test, we can automatically preserve the
    // 'session_id' and 'remember_token' cookies. 
    Cypress.Cookies.preserveOnce('csrftoken', 'sessionid')
  })
    
    // // Logging in
    // it('Logging in', () => {
    //     cy.visit('http://127.0.0.1:8000/')

    //     cy.get('#username')
    //       .type('test')
    //       .should('have.value', 'test')

    //     cy.get('#password')
    //       .type('tanuki404')
    //       .should('have.value', 'tanuki404')

    //     cy.get('.userinfo')
    //       .find('form').submit()

    //     cy.get('#budget1').click()

    //     cy.url().should('eq', 'http://127.0.0.1:8000/budget/')
    // })

    // users can add items to income
    it('users can add items to income', () => {
        cy.get('#id_itemDate')
          .type('11/5/2020')
          .should('have.value', '11/5/2020')
        
        cy.get('#id_itemName')
          .type('Piggybank')
          .should('have.value', 'Piggybank')

        cy.get('#id_itemAmount')
          .type('200')
          .should('have.value', '200')

        cy.get('#id_itemAmount')
          .type('{enter}')
    })

    // users can delete items in income
    it('users can delete items in income', () => {
        
    })

    // users can add items to fixed expenses
    it('users can add items to fixed expenses', () => {
        
    })

    // users can delete items in income
    it('users can delete items in income', () => {
        
    })

    // users can adjust where their additional spending goes

    // users can modify their items in various sections
    // Adjusting additional spending is shown in progress bars in the home page
    
    // Summary is calculated correctly
    it('Available cash is calculated correctly', () => {
        
    })

    // users should be able to navigate to other pages and log out

})
