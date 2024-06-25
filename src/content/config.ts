import { z, defineCollection } from 'astro:content'

const avio = defineCollection({
	type: 'content',
	schema: z.object({
		title: z.string(),
		category: z.string(),
		featured: z.number().optional().default(0),
		image: z.string().optional(),
		created: z.coerce.date(),
		updated: z.coerce.date(),
		created_by: z.string().optional().default("Ignazio"),
	}),
})

const posts = defineCollection({
	type: 'content',
	schema: z.object({
		id: z.number(),
		title: z.string(),
		description: z.string().optional(),
		category: z.string(),
		featured: z.number().optional().default(0),
		image: z.string().optional(),
		created: z.coerce.date(),
		updated: z.coerce.date(),
		created_by: z.string().optional().default("Ignazio"),
	}),
})

const market = defineCollection({
	type: 'content',
	schema: z.object({
		id: z.number(),
		title: z.string(),
		description: z.string(),
		featured: z.number().optional().default(0),
		image: z.string().optional(),
		created: z.coerce.date(),
		updated: z.coerce.date(),
		created_by: z.string().optional().default("Ignazio"),
	})
})

const meteo = defineCollection({
	type: 'content',
	schema: z.object({
		title: z.string().optional(),
		pics: z.array(z.string()),
	})
})

export const collections = {
	avio,
	posts,
	meteo,
	market
}
