import React from 'react'
import logo from '../../images/logo.png'
const HomePage = () => {
    return (
        <div>
   <header className='center'>
        <img src={logo} alt='/'/>
    
    </header>
<section className='search'>
      <form>
        <input
          type='text'
          className='form-control'
          placeholder='Search for a github repo'
        //   value={text}
        //   onChange={(e) => onChange(e.target.value)}
          autoFocus
        />
      </form>
    </section>
        </div>
 
    
    )
}

export default HomePage
