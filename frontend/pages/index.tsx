import type { GetServerSideProps, GetStaticProps, NextPage } from 'next'
import 'semantic-ui-css/semantic.min.css'
import { gql, useQuery } from "@apollo/client";
import client from '../graphql/apollo-client';
import styles from "../styles/Home.module.css";

interface Country {
  id: string;
  jpName: string;
  enName: string;
}

interface CountriesProps {
  countries: Country[];
}

const fetchCountries = async (): Promise<CountriesProps> => {
  const { data } = await client.query({
    query: gql`
      query Countries {
        countries {
          id
          jpName
          enName
        }
      }
    `,
  })

  return data;
}

// export const getStaticProps: GetStaticProps<BooksProps> = async () => {
//   const { data } = await client.query({
//     query: gql`
//       query Books {
//         books {
//           title
//           author {
//             name
//           }
//         }
//       }
//     `,
//   })
//   // .then(result => console.log(result))
//   // .catch(error => {
//   //   return { data: error}
//   // });

//   // console.log(data);

//   return {
//     props: {
//       books: data.books,
//     }
//   }
// }

const Home: NextPage<CountriesProps> = ({ countries }) => {
  console.log(countries);
  return (
      <div className={styles.grid}>
        <ul>
          {countries.map((country: Country) => (
            <div key={country.id} className={styles.card}>
              <li>{country.id} - {country.jpName} - {country.enName}</li>
            </div>
          ))}
        </ul>
      </div>
  )
}

export const getServerSideProps: GetServerSideProps<
  CountriesProps
> = async () => {
  const data: CountriesProps = await fetchCountries();
  return {
    props: {
      countries: data.countries
    }
  }
};

export default Home
