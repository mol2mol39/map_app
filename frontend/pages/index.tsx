import type { GetServerSideProps, GetStaticProps, NextPage } from 'next'
import 'semantic-ui-css/semantic.min.css'
import { gql, useQuery } from "@apollo/client";
import client from '../graphql/apollo-client';
import styles from "../styles/Home.module.css";

interface Author {
  name: string;
}

interface Book {
  title: string;
  author: Author;
}

interface BooksProps {
  books: Book[];
}

const fetchCountries = async (): Promise<BooksProps> => {
  const { data } = await client.query({
    query: gql`
      query Books {
        books {
          title
          author {
            name
          }
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

const Home: NextPage<BooksProps> = ({ books }) => {
  console.log(books);
  return (
      <div className={styles.grid}>
        <ul>
          {books.map((book: Book) => (
            <div key={book.title} className={styles.card}>
              <li>{book.title} - {book.author.name}</li>
            </div>
          ))}
        </ul>
      </div>
  )
}

export const getServerSideProps: GetServerSideProps<
  BooksProps
> = async () => {
  const data: BooksProps = await fetchCountries();
  return {
    props: {
      books: data.books
    }
  }
};

export default Home
